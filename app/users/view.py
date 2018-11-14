#!flask/bin/python#!flask/bin/python
from flask_restful import Resource
from flask import jsonify

class UserView(Resource):
	""" Main Class """

	def success(self, msg):
		message = { 
			'status': 201,  
			'message':  msg }
		resp = jsonify(message)
		resp.status_code = 201
		return resp

	def error(self, msg):
		message = { 
			'error': True,
			'status': 501,  
			'message':  msg }
		resp = jsonify(message)
		resp.status_code = 501
		return resp