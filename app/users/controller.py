#!flask/bin/python
from flask_restful import Resource
from app.users.view import UserView
from flask import request, json
from app.users.model import User
from app.db import db
from pycpfcnpj import cpfcnpj, compatible
from app.users.exceptions import CpfInvalido
from app.enum import Messages
from pycpfcnpj import cpfcnpj	

class UserSituacao(Resource):
	""" User Status Class """

	""" Update status """
	def put(self):
		dataDict = json.loads(request.data)
		user = User.query.filter(User.id==dataDict["id"]).first()
		res = ""
		if user:
			if user.situacao == "I":
				user.situacao = "A"
				res = Messages.MN033.value

			elif user.situacao == "A":
				user.situacao = "I"
				res = Messages.MN032.value

			db.session.commit()

			return UserView.success(self, res)

class UserApi(Resource):
	""" User Api Class """

	""" Get Users """
	def get(self):
		res = []
		users = User.query.filter()
		if users:
			for user in users:
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
		return UserView.success(self, res)

	""" Update user """
	def put(self):
		dataDict = json.loads(request.data)
		user = User.query.filter(User.id==dataDict["id"]).first()	
		if user:
			if 'usuario' in dataDict and dataDict['usuario']:
				user.usuario = dataDict['usuario']

			if 'email' in dataDict and dataDict['email']:
				user.email = dataDict['email']

			if 'perfil_acesso' in dataDict and dataDict['perfil_acesso']:
				user.perfil_acesso = dataDict['perfil_acesso']['id']

			if 'funcao' in dataDict and dataDict['funcao']:	
				user.funcao = dataDict['funcao']['id']

			if 'telefone' in dataDict and dataDict['telefone']:
				user.telefone = dataDict['telefone']

			
			db.session.commit()
		return UserView.success(self, Messages.MN030.value)

	""" Insert new user """
	def post(self):
		dataDict = json.loads(request.data)

		if not cpfcnpj.validate(dataDict["cpf"]):
			return UserView.error(self, Messages.MN035.value)

		user = User.query.filter(User.cpf==compatible.clear_punctuation(dataDict["cpf"])).first()
		if not user:

			user = User(
				usuario=dataDict["usuario"],
				email=dataDict["email"],
				cpf=compatible.clear_punctuation(dataDict["cpf"]),
				situacao=dataDict["situacao"]['id'],
				perfil_acesso=dataDict["perfil_acesso"]['id'],
				funcao=dataDict["funcao"]['id'],
				telefone=dataDict["telefone"],
				)
			
			db.session.add(user)
			db.session.commit()
			return UserView.success(self, Messages.MN001.value)
		else:
			return UserView.error(self, Messages.MN034.value)

	""" Delete user """	
	def delete(self):
		id = request.args.get('id')
		user = User.query.filter(User.id==id).first()
		if user:
			db.session.delete(user)
			db.session.commit()
			return UserView.success(self, Messages.MN005.value)