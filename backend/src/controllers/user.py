import logging
from datetime import datetime
from uuid import uuid4

from src.controllers.controller import Controller
from src.controllers.errors.login_failure import LoginFailure
from src.controllers.errors.user_not_found import UserNotFound
from src.models.user import User


class UserController(Controller):
    def __init__(self) -> None:
        self.__users = []
        logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

    def create(self, login: str, password: str) -> str:
        # Verificando se o login ja e utilizado
        for user in self.__users:
            if(user.login == login and user.deleted_at == None):
                raise LoginFailure("Este login ja esta em uso")

        id = str(uuid4())
        user = User(id, login, password)
        self.__users.append(user)
        logging.warning(f'Usuario {login} criado')
        return id

    def find(self, id) -> User:
        user = self.find_by_id(id)
        if (user):
            logging.warning(f'Usuario {user.login} procurada')
            return user.as_dict()

        raise UserNotFound(f"user {id} not found")

    def find_all(self) -> list:
        ''' itera em toda a lista de users. 
        transforma cada elemento em um dicionario
        se ele não estiver deletado'''
        logging.warning('Lista de usuarios apresentada')
        return [user.as_dict() for user in self.__users if user.deleted_at == None]

    def update(self, login: str, password: str, new_password: str, user) -> str:
        for item in self.__users:
            if (item.login == login and item.password == password):
                item.password = new_password
                item.updated_at = datetime.now()
                item.updated_by = user
                logging.warning(f'Password do {item.login} alterado')
                return str('Password alterado com sucesso')

        return str('Login ou Password incorretos')

    def delete(self, id: str, user: str) -> str:
        for item in self.__users:
            if (item.id == id and item.deleted_at == None):
                item.deleted_at = datetime.now()
                item.deleted_by = user
                logging.warning(f'Usuario {item.login} deletado')
                return str("usuario deletado")

        return str("usuario nao encontrado")

    def login(self, login: str, password: str):
        for user in self.__users:
            if user.login == login and user.password == password and user.deleted_at == None:
                logging.warning(f'Login {user.login}')
                return user.id
        raise LoginFailure(f"failed to login {login}")

    def find_by_id(self, id: str) -> User:
        for user in self.__users:
            if user.id == id and user.deleted_at == None:
                logging.warning(f'User by id {user} procurado')
                return user
        raise UserNotFound(f"user {id} not found")
