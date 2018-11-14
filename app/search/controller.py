#!flask/bin/python
from flask_restful import Resource
from app.search.view import SearchView
from flask import request, json
from app.users.model import User
from app.db import db

class Search(Resource):
	""" User Class """

	""" Search """
	def post(self):
		res = []
		dataDict = json.loads(request.data)	


		users = User.query.filter()

		if 'usuario' in dataDict and dataDict['usuario']:
			print(dataDict['usuario'])
			users = users.filter(User.usuario.like("%"+dataDict['usuario']+"%"))

		if 'situacao' in dataDict and dataDict['situacao']:
			print(dataDict['situacao'])
			users = users.filter(User.situacao == dataDict['situacao'])
		
		if 'perfil_acesso' in dataDict and dataDict['perfil_acesso']:
			print(dataDict['perfil_acesso'])
			users = users.filter(User.perfil_acesso == dataDict['perfil_acesso'])
		
		if users:
			for user in users:
				print(user.usuario)
				res.append({
					"id": user.id,
					"usuario": user.usuario,
					"email": user.email,
					"cpf": user.cpf,
					"situacao": user.situacao,
					"perfil_acesso": user.perfil_acesso,
					"funcao": user.funcao,
					"telefone": user.telefone
					})
		
		return SearchView.success(self, res)

	""" Get Users """
	def get(self):
		res = []
		id = request.args.get('id')
		user = User.query.filter(User.id == id).first()
		if user:
			res = {
				"id": user.id,
				"usuario": user.usuario,
				"email": user.email,
				"cpf": user.cpf,
				"situacao": user.situacao,
				"perfil_acesso": user.perfil_acesso,
				"funcao": user.funcao,
				"telefone": user.telefone
				}
		return SearchView.success(self, res)