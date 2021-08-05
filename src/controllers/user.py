from src.models.user import User
from uuid import uuid4


class UserController():
    def __init__(self) -> None:
        self.__users = []
        self.__deleted = []

    def create(self, login: str, password: str) -> str:
        for user in self.__users:
            if(user.login == login):
                return str("Este login ja esta em uso")

        id = str(uuid4())
        user = User(id, login, password)
        self.__users.append(user)
        return id

    def find(self, id) -> User:
        for user in self.__users:
            if (user.id == id):
                return user.as_dict()

        return None

    def find_all(self) -> list:
        return [user.as_dict() for user in self.__users]

    def update(self, login: str, password: str, new_password: str) -> str:

        for user in self.__users:
            if (user.login == login and user.password == password):
                user.password = new_password
                return str('Password alterado com sucesso')

        return str('Login ou Password incorretos')

    def delete(self, id: str) -> str:
        for user in self.__users:
            if (user.id == id):
                self.__deleted.append(user)
                self.__users.remove(user)
                return str("usuario deletado")

        return str("usuario nao encontrado")
