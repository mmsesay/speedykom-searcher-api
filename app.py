"""
Filename        :   app.py
Description     :   This file contains the whole logic for the application
Author          :   Muhammad Sesay
Email           :   contact@maej.dev
Started writing :   8/March/2023
Completed on    :   in progress
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src.fetcher import get_data_from_health_gov

app = Flask(__name__)

# app secret key
app.config['SECRET_KEY'] = 'devkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route("/api/v1/search/<keyword>", methods=['GET'])
def search_keyword(keyword):
    """
    Fetches data from health gov health finder
    :params keyword: this is the keyword to query
    :return : the response from the invoked function
    """
    return get_data_from_health_gov(keyword)


if __name__ == '__main__':
    app.run()