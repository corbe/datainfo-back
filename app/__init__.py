from flask import Flask, Blueprint

from flask_restful import Api
from flask_cors import CORS
from app.config import app_config
from app.users.controller import UserSituacao, UserApi
from app.search.controller import Search

from app.db import db


def create_app(config_name):
	app = Flask(__name__, instance_relative_config=True)
	CORS(app)
	app.config.from_object(app_config['development'])
	app.config.from_pyfile('config.py')

	api_bp = Blueprint('api', __name__)                                              
	api =  Api(api_bp)

	api.add_resource(UserApi, '/user')
	api.add_resource(UserSituacao, '/user/situacao')
	api.add_resource(Search, '/search')

	app.register_blueprint(api_bp)

	

	db.init_app(app)


	return app