# __init__.py
"""
Filename        :   __init__.py
Description     :   This file contains the whole logic for the application
Author          :   Muhammad Sesay
Email           :   contact@maej.dev
Started writing :   8/March/2023
Completed on    :   in progress
"""
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# app secret key
app.config['SECRET_KEY'] = 'devkey'
app.config["JWT_SECRET_KEY"] = "testsecretkey"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.root_path, 'users.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from app import routes

if __name__ == "__main__":
  app.run(debug=True)
