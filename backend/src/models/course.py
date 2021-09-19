from bson.objectid import ObjectId
from src.models.university import University
from src.models.timestamp import Timestamp
from datetime import datetime


class Course(Timestamp):
    def __init__(self, id: ObjectId, name: str, university: ObjectId, created_by: ObjectId, created_at: datetime, updated_by: ObjectId = None, updated_at: datetime = None, deleted_by: ObjectId = None, deleted_at: datetime = None) -> None:
        super().__init__()
        self.__id = id
        self.__name = name
        self.__university = university
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
            'university': self.__university,
            'created_by': self.created_by,
            'created_at': self.created_at,
            'updated_by': self.updated_by,
            'updated_at': self.updated_at,
            'deleted_by': self.deleted_by,
            'deleted_at': self.deleted_at
        }



    def as_dict(self):
        return {
            'id': str(self.__id),
            'name': self.__name,
            'university': str(self.__university),
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
    def university(self) -> University:
        return self.__university

    @university.setter
    def university(self, university: University):
        self.__university = university

    
