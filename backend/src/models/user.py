from src.models.timestamp import Timestamp
from datetime import datetime


class User(Timestamp):
    def __init__(self, id: str, login: str, password: str, created_at, updated_by=None, updated_at=None, deleted_at=None, deleted_by=None) -> None:
        super().__init__()
        self.__id = id
        self.__login = login
        self.__password = password
        self.created_at = created_at
        self.updated_by = updated_by
        self.updated_at = updated_at
        self.deleted_at = deleted_at
        self.deleted_by = deleted_by

    def as_dict(self):
        return {
            '_id': self.__id,
            'login': self.__login,
            'password': self.password,
            'created_at': self.created_at,
            'updated_by': self.updated_by.as_dict() if self.updated_by else None,
            'updated_at': self.updated_at,
            'deleted_by': self.deleted_by.as_dict() if self.deleted_by else None,
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
