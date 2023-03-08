import os
import tempfile
import pytest
import unittest

from app import app, db


# @pytest.fixture
# def client():
#     db_fd, app.config['DATABASE'] = 'sqlite:///users.db' # tempfile.mkstemp()
#     app.config['TESTING'] = True

#     with app.test_client() as client:
#         with app.app_context():
#             app.init_db()
#         yield client

#     os.close(db_fd)
#     os.unlink(app.config['DATABASE'])

class StartupTest(unittest.TestCase):
    # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
            os.path.join(app.root_path, 'user.db')
        self.app = app.test_client()
        db.create_all()
 
 
    # executed after each test
    def tearDown(self):
        db.drop_all()


if __name__ == "__main__":
    unittest.main()