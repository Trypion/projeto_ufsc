from datetime import datetime
from bson.objectid import ObjectId
from src.models.timestamp import Timestamp


class University(Timestamp):
    def __init__(self, id: ObjectId, name: str, uf: str, created_by: ObjectId, created_at: datetime, updated_by: ObjectId = None, updated_at: datetime = None, deleted_by: ObjectId = None, deleted_at: datetime = None) -> None:
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

    def serialize(self):
        return {
            '_id': self.__id,
            'name': self.__name,
            'uf': self.__uf,
            'created_by': self.created_by,
            'created_at': self.created_at,
            'updated_by': self.updated_by,
            'updated_at': self.updated_at,
            'deleted_by': self.deleted_by,
            'deleted_at': self.deleted_at
        }
    
    def as_dict(self):
        return {
            '_id': str(self.__id),
            'name': self.__name,
            'uf': self.__uf,
            'created_by': str(self.created_by),
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
