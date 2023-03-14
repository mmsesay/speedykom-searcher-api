"""
Filename        :   test_main.py
Description     :   This file contains tests
Author          :   Muhammad Sesay
Email           :   contact@maej.dev
Started writing :   8/March/2023
Completed on    :   in progress
"""
import os
import json
import unittest

from app import app, db
from app.models import User


class StartupTest(unittest.TestCase):
    # executed prior to each test
    def setUp(self):
        with app.app_context():
            app.config['TESTING'] = True
            app.config['WTF_CSRF_ENABLED'] = False
            app.config['DEBUG'] = False
            app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.root_path, 'users.sqlite3')
            self.client = app.test_client()
            db.create_all()
 
 
    # executed after each test
    def tearDown(self):
        with app.app_context():
            db.drop_all()

    def test_saving_user(self):
        """Test user saves successfully"""
        with app.app_context():
            user = User(
                email='test@test.com',
                password='test'
            )
        
            db.session.add(user)
            db.session.commit()

            assert user in db.session

    def test_registration(self):
        """ Test for user registration """

        response = self.client.post(
            '/api/v1/register',
            data = json.dumps(dict(
                email='test@test.com',
                password='123456'
            )),
            content_type='application/json'
        )
        data = json.loads(response.data)
        print(data['status'])
        self.assertTrue(data['status'] == 200)
        self.assertTrue(data['message'] == 'Successfully registered.')
        self.assertEqual(response.status_code, 201)



if __name__ == "__main__":
    unittest.main()