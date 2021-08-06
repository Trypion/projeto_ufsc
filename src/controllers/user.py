from uuid import uuid4
from datetime import datetime

from src.controllers.controller import Controller

from src.models.user import User

class UserController(Controller):
    def __init__(self) -> None:
        self.__users = []

    def create(self, login: str, password: str) -> str:
        for user in self.__users:
            if(user.login == login and user.deleted_at == None):
                return str("Este login ja esta em uso")

        id = str(uuid4())
        user = User(id, login, password)
        self.__users.append(user)
        return id

    def find(self, id) -> User:
        for user in self.__users:
            if (user.id == id and user.deleted_at == None):
                return user.as_dict()

        return None

    def find_all(self) -> list:
        ''' itera em toda a lista de users. 
        transforma cada elemento em um dicionario
        se ele não estiver deletado'''
        return [user.as_dict() for user in self.__users if user.deleted_at == None]

    def update(self, login: str, password: str, new_password: str, user) -> str:

        for item in self.__users:
            if (item.login == login and item.password == password):
                item.password = new_password
                item.updated_at = str(datetime.now())
                item.updated_by = user
                return str('Password alterado com sucesso')

        return str('Login ou Password incorretos')

    def delete(self, id: str, user: str) -> str:
        for item in self.__users:
            if (item.id == id and item.deleted_at == None):
                item.deleted_at = str(datetime.now())
                item.deleted_by = user
                return str("usuario deletado")

        return str("usuario nao encontrado")
