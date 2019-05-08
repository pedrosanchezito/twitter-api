from flask_restplus import Namespace, Resource, fields
from flask import Flask, render_template
from app.models import User
from app import db

api = Namespace('users')

json_user = api.model('User', {
    'id': fields.Integer,
    'username': fields.String,
    'password': fields.String,
    'email': fields.String,
    'key': fields.String
})

json_new_user = api.model('New user', {
    'username': fields.String(required=True),
    'password': fields.String(required=True),
    'email': fields.String(required=True)
})

@api.route('')
@api.response(422, 'Invalid request')
class UserResource(Resource):

    def get(self):
        return render_template('register.html')

    @api.marshal_with(json_user, code=201)
    @api.expect(json_new_user, validate=True)
    def post(self):
        username = api.payload['username']
        password = api.payload['password']
        email = api.payload['email']
        user = User(username=username, password=password, email=email)
        db.session.add(user)
        db.session.commit()
        return user, 201

@api.route('/<int:id>')
@api.response(404, 'User not found')
@api.param('id', 'The user unique identifier')
class UserResource(Resource):

    @api.marshal_with(json_user)
    def get(self, id):
        user = db.session.query(User).get(id)
        if user is None:
            api.abort(404, "User {} doesn't exist".format(id))
        else:
            return user, 200

    @api.marshal_with(json_user, code=201)
    @api.expect(json_new_user, validate=True)
    def patch(self, id):
        user = db.session.query(User).get(id)
        if user is None:
            api.abort(404, "User {} doesn't exist".format(id))
        else:
            user.username = api.payload['username']
            user.password = api.payload['password']
            user.email = api.payload['email']
            db.session.commit()
            return user, 201
