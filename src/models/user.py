from src.models.timestamp import Timestamp
from datetime import datetime


class User(Timestamp):
    def __init__(self, id: str, login: str, password: str) -> None:
        super().__init__()
        self.__id = id
        self.__login = login
        self.__password = password
        self.__profile_id = None
        self.created_at = datetime.now()

    def as_dict(self):
        return {
            'id': self.__id,
            'login': self.__login,
            'password': self.__password,
            'created_at': self.created_at,
            'updated_by': self.updated_by,
            'updated_at': self.updated_at,
            'deleted_by': self.deleted_by,
            'deleted_at': self.deleted_at
        }
    @property
    def profile_id(self):
        return self.__profile_id
    
    @profile_id.setter
    def profile_id(self, profile_id):
        self.__profile_id = profile_id

    @property
    def id(self) -> str:
        return self.__id

    @property
    def login(self) -> str:
        return self.__login

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password
    