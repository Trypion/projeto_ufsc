from bson.objectid import ObjectId
from src.models.timestamp import Timestamp
from datetime import datetime


class User(Timestamp):
    def __init__(self, id: ObjectId, login: str, password: str, created_at: datetime, updated_by: ObjectId = None, updated_at: datetime = None, deleted_at: datetime = None, deleted_by: ObjectId = None) -> None:
        super().__init__()
        self.__id = id
        self.__login = login
        self.__password = password
        self.created_at = created_at
        self.updated_by = updated_by
        self.updated_at = updated_at
        self.deleted_at = deleted_at
        self.deleted_by = deleted_by

    def serialize(self):
        return {
            '_id': self.__id,
            'login': self.__login,
            'password': self.__password,
            'created_at': self.created_at,
            'updated_by': self.updated_by,
            'updated_at': self.updated_at,
            'deleted_by': self.deleted_by,
            'deleted_at': self.deleted_at
        }

    def as_dict(self):
        return {
            '_id': str(self.__id),
            'login': self.__login,
            'created_at': self.created_at,
            'updated_by': str(self.updated_by),
            'updated_at': self.updated_at,
            'deleted_by': str(self.deleted_by),
            'deleted_at': self.deleted_at
        }

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
