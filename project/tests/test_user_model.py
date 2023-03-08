# import unittest

# from project.app import db
# from project.app.models import User
# # from flask_testing import TestCase


# class TestUserModel(TestCase):

#     def test_encode_auth_token(self):
#         user = User(
#             email='test@test.com',
#             password='test'
#         )
#         db.session.add(user)
#         db.session.commit()
#         assert user in db.session
#         # auth_token = user.encode_auth_token(user.id)
#         # self.assertTrue(isinstance(auth_token, bytes))

# if __name__ == '__main__':
#     unittest.main()
