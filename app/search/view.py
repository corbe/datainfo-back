#!flask/bin/python
from flask_restful import Resource
from flask import jsonify

class SearchView(Resource):
	""" Main Class """

	def success(self, msg):
		message = { 
			'status': 201,  
			'message':  msg }
		resp = jsonify(message)
		resp.status_code = 201
		return resp\
