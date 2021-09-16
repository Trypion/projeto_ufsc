from src.models.timestamp import Timestamp
from src.models.user import User

from datetime import datetime


class University(Timestamp):
    def __init__(self, id: str, name: str, uf: str, created_by, created_at, updated_by = None, updated_at = None, deleted_by = None, deleted_at = None) -> None:
        super().__init__()
        self.__id = id
        self.__name = name
        self.__uf = uf
        self.created_at = created_at
        self.created_by = created_by
        self.updated_by = updated_by
        self.updated_at = updated_at
        self.deleted_by = deleted_by
        self.deleted_at = deleted_at

    def as_dict(self):
        return {
            'id': self.__id,
            'name': self.__name,
            'uf': self.__uf,
            'created_by': self.created_by.as_dict(),
            'created_at': self.created_at,
            'updated_by': self.updated_by.as_dict() if self.updated_by else None,
            'updated_at': self.updated_at,
            'deleted_by': self.deleted_by.as_dict() if self.deleted_by else None,
            'deleted_at': self.deleted_at
        }

    @property
    def id(self) -> str:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @property
    def uf(self) -> str:
        return self.__uf

    @uf.setter
    def uf(self, uf: str) -> None:
        self.__uf = uf
