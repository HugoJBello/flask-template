import os

from flask import Flask
from flask_restful import Resource, Api
from app.auth import Login
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)

app_settings = os.getenv(
    'APP_SETTINGS',
    'app.config.DevelopmentConfig'
)
app.config.from_object(app_settings)


CORS(app)
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')
api.add_resource(Login, '/auth/login')


if __name__ == '__main__':
    app.run(debug=True)