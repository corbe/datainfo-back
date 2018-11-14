from enum import Enum

class Messages(Enum):
	MN001= "Cadastro efetuado com sucesso!"
	MN005= "Exclusão efetuada com sucesso."
	MN030= "Alteração efetuada com sucesso!"
	MN031= "Deseja realmente excluir o usuário <Nome do Usuário>?"
	MN032= "Usuário desabilitado com sucesso!"
	MN033= "Usuário habilitado com sucesso!"
	MN034= "Operação não realizada. Usuário já incluído."
	MN035= "Operação não realizada. CPF digitado é inválido."