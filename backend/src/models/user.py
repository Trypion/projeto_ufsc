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
            '_id': self.__id,
            'login': self.__login,
            'password': self.password.decode(),         
            'created_at': datetime.strftime(self.created_at, "%d/%m/%Y"),
            'updated_by': self.updated_by.as_dict() if self.updated_by else None,
            'updated_at': datetime.strftime(self.updated_at, "%d/%m/%Y") if self.updated_at else None,
            'deleted_by': self.deleted_by.as_dict() if self.deleted_by else None,
            'deleted_at': datetime.strftime(self.deleted_at, "%d/%m/%Y") if self.deleted_at else None,
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
    