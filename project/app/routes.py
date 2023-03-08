from flask import (jsonify, request, make_response)
from app import app, db
from app.fetcher import get_data_from_health_gov
from app.models import User

@app.route("/api/v1/search/<keyword>", methods=['GET'])
def search_keyword(keyword):
    """
    Fetches data from health gov health finder
    :params keyword: this is the keyword to query
    :return : the response from the invoked function
    """
    return get_data_from_health_gov(keyword)


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

            # generate the auth token
            auth_token = user.encode_auth_token(user.id)
            responseObject = {
                'status': 'success',
                'message': 'Successfully registered.',
                'auth_token': auth_token.decode()
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


@app.route("/api/v1/hello", methods=['GET'])
def index():
    """
    Fetches data from health gov health finder
    :params keyword: this is the keyword to query
    :return : the response from the invoked function
    """
    return jsonify({
        "status": 200,
        "data": "Hello"
    })