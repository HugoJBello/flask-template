# project/server/__init__.py

import os

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_restful import Resource, Api
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
CORS(app)
api = Api(app)


app_settings = os.getenv(
    'APP_SETTINGS',
    'project.server.config.DevelopmentConfig'
)
app.config.from_object(app_settings)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

bcrypt = Bcrypt(app)
db = SQLAlchemy(app)

from project.server.auth.views import auth_blueprint
app.register_blueprint(auth_blueprint)
