#!flask/bin/python
from flask import Flask, Blueprint
from flask_restful import Api, Resource, url_for
from main.view import MainView

app = Flask(__name__)
api_bp = Blueprint('api', __name__)
api = Api(api_bp)

class Main(Resource):
	""" Main Class """

	""" Get Method """
	def get(self):
		msg = "success"
		return MainView.success(self, msg)


api.add_resource(Main, '/')
app.register_blueprint(api_bp)