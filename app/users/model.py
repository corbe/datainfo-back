from flask_sqlalchemy import SQLAlchemy
from app.db import db

class User(db.Model):

    __tablename__ = 'usuario_externo'

    id = db.Column("nu_id",db.Integer, primary_key=True)
    usuario = db.Column("no_usuario",db.String(60), unique=False, nullable=False)
    email = db.Column("de_email", db.String(255), unique=False, nullable=False)
    cpf = db.Column("nu_cpf",db.String(11), unique=False, nullable=False)
    situacao = db.Column("ic_situacao", db.String(1), unique=False, nullable=False)
    perfil_acesso = db.Column("ic_perfil_acesso", db.String(30), unique=False, nullable=False)
    funcao = db.Column("co_funcao", db.String(30), unique=False, nullable=False)
    telefone = db.Column("nu_telefone", db.String(11), unique=False, nullable=True)

    def __repr__(self):
        return '<User %r>' % self.usuario


