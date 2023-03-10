"""
Filename        :   routes.py
Description     :   This file contains the whole logic for the registation, login and search
Author          :   Muhammad Sesay
Email           :   contact@maej.dev
Started writing :   8/March/2023
Completed on    :   in progress
"""
from datetime import timedelta
from flask import (jsonify, request, make_response)
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

from app import app, db
from app.fetcher import get_data_from_health_gov, get_single_data_from_health_gov, get_all_data_from_health_gov
from app.models import User

jwt = JWTManager(app)

@app.route("/api/v1/records/search/<keyword>", methods=['GET'])
@jwt_required()
def search_record_by_keyword(keyword):
    """
    Fetches data from health gov health finder
    :params keyword: this is the keyword to query
    :return : the response from the invoked function
    """

    current_user = get_jwt_identity()
    user = User.query.filter_by(id=current_user).first()

    if user:
        return get_data_from_health_gov(keyword)
    else:
        responseObject = {
            'status': 'error',
            'message': 'Provide a valid auth token.'
        }
        return make_response(jsonify(responseObject)), 401


@app.route("/api/v1/records/<id>", methods=['GET'])
@jwt_required()
def single_records(id):
    """
    Fetches single data from health gov health finder
    :params id: this is the id to query
    :return : the response from the invoked function
    """

    current_user = get_jwt_identity()
    user = User.query.filter_by(id=current_user).first()

    if user:
        return get_single_data_from_health_gov(id)
    else:
        responseObject = {
            'status': 'error',
            'message': 'Provide a valid auth token.'
        }
        return make_response(jsonify(responseObject)), 401


@app.route("/api/v1/records", methods=['GET'])
@jwt_required()
def all_records(id):
    """
    Fetches all data from health gov health finder
    :return : the response from the invoked function
    """

    current_user = get_jwt_identity()
    user = User.query.filter_by(id=current_user).first()

    if user:
        return get_all_data_from_health_gov
    else:
        responseObject = {
            'status': 'error',
            'message': 'Provide a valid auth token.'
        }
        return make_response(jsonify(responseObject)), 401


@app.route("/api/v1/register", methods=['POST'])
def register():
    """
    Receives form post and create record
    :params form: receives the form data
    :return : the response
    """

    # get the post data
    post_data = request.get_json()

    # check if user already exists
    user = User.query.filter_by(email=post_data.get('email')).first()
    if not user:
        try:
            user = User(
                email=post_data.get('email'),
                password=post_data.get('password')
            )

            # insert the user
            db.session.add(user)
            db.session.commit()

            responseObject = {
                'status': 'success',
                'message': 'Successfully registered.'
            }
            return make_response(jsonify(responseObject)), 201
        except Exception as e:
            responseObject = {
                'status': 'fail',
                'message': 'Some error occurred. Please try again.'
            }
            return make_response(jsonify(responseObject)), 401
    else:
        responseObject = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return make_response(jsonify(responseObject)), 202


@app.route("/api/v1/login", methods=['POST'])
def login():
    """
    Fetches data from health gov health finder
    :params keyword: this is the keyword to query
    :return : the response from the invoked function
    """

    # handle post request
    if request.method == "POST":
        # get the post data
        post_data = request.get_json()

        # check if user already exists
        user = User.query.filter_by(email=post_data.get('email')).first()

        if user is None or not user.verify_password(post_data.get('password')):
            return make_response(jsonify({
                'status': 'error',
                'message': 'Invalid username or password'
            })), 404
        
        # login the user encode_auth_token(user.id) # 
        auth_token = create_access_token(identity=user.id, expires_delta=timedelta(hours=1)) # encode_auth_token(user.id)

        return make_response(jsonify({
            'status': 'success',
            'message': 'login successful',
            "auth_token": auth_token
        })), 200
    else:
        return make_response(jsonify({
            'status': 'error',
            'message': 'Only post method is allowed'
        })), 500