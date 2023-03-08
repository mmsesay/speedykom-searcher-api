import os
import json
import unittest

from app import app, db


class StartupTest(unittest.TestCase):
    # executed prior to each test
    def setUp(self):
        with app.app_context():
            app.config['TESTING'] = True
            app.config['WTF_CSRF_ENABLED'] = False
            app.config['DEBUG'] = False
            app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.root_path, 'users.db')
            self.client = app.test_client()
            db.create_all()
 
 
    # executed after each test
    def tearDown(self):
        with app.app_context():
            db.drop_all()
        # pass

    def test_hello_page(self):
        """Validate empty user login fields"""
        response = self.client.get("/api/v1/hello")
        jsondata = json.loads(response.get_data(as_text=True))
        self.assertEquals('Hello', jsondata['data'])
        # self.assertIn(b'H', response.data)

if __name__ == "__main__":
    unittest.main()