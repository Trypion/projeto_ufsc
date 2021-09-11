from src.models.timestamp import Timestamp
from src.models.user import User

from datetime import datetime


class University(Timestamp):
    def __init__(self, id: str, name: str, uf: str, user: User) -> None:
        super().__init__()
        self.__id = id
        self.__name = name
        self.__uf = uf
        self.created_at = datetime.now()
        self.created_by = user

    def as_dict(self):
        return {
            'id': self.__id,
            'name': self.__name,
            'uf': self.__uf,
            'created_by': self.created_by.as_dict(),
            'created_at': datetime.strftime(self.created_at, "%d/%m/%Y"),
            'updated_by': self.updated_by.as_dict() if self.updated_by else None,
            'updated_at': datetime.strftime(self.updated_at, "%d/%m/%Y") if self.updated_at else None,
            'deleted_by': self.deleted_by.as_dict() if self.deleted_by else None,
            'deleted_at': datetime.strftime(self.deleted_at, "%d/%m/%Y") if self.deleted_at else None,
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
