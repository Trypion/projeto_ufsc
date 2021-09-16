
from datetime import datetime
from src.controllers.errors.invalid_password import InvalidPassword
# from uuid import uuid4
from bson import ObjectId
import bcrypt

from src.models.user import User
from src.DAO.user import UserDAO
from src.controllers.controller import Controller
from src.controllers.errors.login_failure import LoginFailure
from src.controllers.errors.user_not_found import UserNotFound


class UserController(Controller):
    def __init__(self, userDAO: UserDAO) -> None:
        self.__userDAO = userDAO

    def create(self, login: str, password: str) -> str:
        # Verificando se o login ja e utilizado
        persisted_user = self.find_by_login(login)
        if persisted_user:
            raise LoginFailure("Este login ja esta em uso")

        hashed = bcrypt.hashpw(
            bytes(password, 'utf-8'), bcrypt.gensalt()).decode('utf-8')

        id = ObjectId()
        user = User(id, login, hashed, datetime.now())
        self.__userDAO.save(user)
        return str(id)

    def find(self, id) -> User:
        user = self.__userDAO.find_by_id(id)
        if (user):
            return user.as_dict()

        raise UserNotFound(f"user {id} not found")

    # legacy code
    def find_all(self) -> list:
        ''' itera em toda a lista de users. 
        transforma cada elemento em um dicionario
        se ele não estiver deletado'''
        return [user.as_dict() for user in self.__users if user.deleted_at == None]

    def change_password(self, login: str, password: str, new_password: str) -> str:
        persisted_user = self.find_by_login(login)

        if (self.__check_password(password, persisted_user.password)):
            persisted_user.password = bcrypt.hashpw(bytes(new_password, 'utf-8'), bcrypt.gensalt()).decode('utf-8')
            self.__userDAO.save(persisted_user)
            return
        
        raise InvalidPassword(f'password invalido')

    def delete(self, id: str, user: User) -> str:
        persisted_user = self.__userDAO.find_by_id(id)
        if (persisted_user):
            persisted_user.deleted_at = datetime.now()
            persisted_user.deleted_by = user
            self.__userDAO.save(persisted_user)
            return

        raise UserNotFound('user not found')
        

    def login(self, login: str, password: str):
        user = self.find_by_login(login)
        if self.__check_password(password, user.password):
            return user.id
        raise LoginFailure(f"failed to login {login}")

    def __check_password(self, password: str, against_passwotd: str) -> bool:
        return bcrypt.checkpw(bytes(password, 'utf-8'), bytes(against_passwotd, 'utf-8'))

    def find_by_login(self, login: str) -> User:
        return self.__userDAO.find_by_login(login)

    def find_by_id(self, id: str) -> User:
        return self.__userDAO.find_by_id(id)

    def update(self):
        ...
