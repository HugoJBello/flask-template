from flask_restful import Resource, reqparse
parser = reqparse.RequestParser()


class Login(Resource):
    def post(self):
        args = parser.parse_args()
        user = args['user'];
        password = args['password']
        return {'hello': user}

class Logout(Resource):
    def post(self):
        return {'hello': 'world'}


class Register(Resource):
    def post(self):
        return {'hello': 'world'}


class isLoggedIn(Resource):
    def post(self):
        return {'hello': 'world'}