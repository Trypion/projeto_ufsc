from src.models.timestamp import Timestamp
from datetime import datetime


class University(Timestamp):
    def __init__(self, id: str, name: str, uf: str, user: str) -> None:
        super().__init__()
        self.__id = id
        self.__name = name
        self.__uf = uf
        self.created_at = str(datetime.now())
        self.created_by = user

    def as_dict(self):
        return {
            'id': self.__id,
            'name': self.__name,
            'uf': self.__uf,
            'created_by': self.created_by,
            'created_at': self.created_at,
            'updated_by': self.updated_by,
            'updated_at': self.updated_at,
            'deleted_by': self.deleted_by,
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
