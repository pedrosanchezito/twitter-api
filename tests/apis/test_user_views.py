from flask_testing import TestCase
from app import create_app, db
from app.models import User

class TestTweetViews(TestCase):
    def create_app(self):
        app = create_app()
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = f"{app.config['SQLALCHEMY_DATABASE_URI']}_test"
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_user_create(self):
        response = self.client.post("/users", json={'username':'test username',
                                                    'password':'testpassword',
                                                    'email':'test@email.com'})
        created_user = response.json
        self.assertEqual(response.status_code, 201)
        self.assertEqual(created_user['username'], 'test username')
        self.assertIsNotNone(created_user['key'])

    def test_user_update_all_details(self):
        first_user = User(username="test_pre",
                            password="password_pre",
                            email="email_pre")
        db.session.add(first_user)
        db.session.commit()
        response = self.client.patch("/users/1", json={'username':'test_post',
                                                    'password':'password_post',
                                                    'email':'email_post'})
        updated_user = response.json
        self.assertEqual(response.status_code, 201)
        self.assertEqual(updated_user['username'], 'test_post')
        self.assertEqual(updated_user['password'], 'password_post')
        self.assertEqual(updated_user['email'], 'email_post')

    def test_user_show_details(self):
        first_user = User(username="test",
                            password="password",
                            email="email")
        db.session.add(first_user)
        db.session.commit()
        response = self.client.get("/users/1")
        response_user = response.json
        self.assertEqual(response_user['username'], 'test')
        self.assertEqual(response_user['password'], 'password')
        self.assertEqual(response_user['email'], 'email')
        self.assertIsNotNone(response_user['key'])
