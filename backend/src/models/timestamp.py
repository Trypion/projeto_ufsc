from abc import ABC, abstractmethod
from datetime import datetime as Date

from bson.objectid import ObjectId

class Timestamp(ABC):
    @abstractmethod 
    def __init__(self) -> None:
        self.__created_at = None
        self.__created_by = None
        self.__updated_at = None
        self.__updated_by = None
        self.__deleted_at = None
        self.__deleted_by= None

    @property
    def created_at(self) -> Date:
        return self.__created_at

    @created_at.setter
    def created_at(self, created_at: Date):
        self.__created_at = created_at

    @property
    def created_by(self) -> ObjectId:
        return self.__created_by

    @created_by.setter
    def created_by(self, created_by: ObjectId):
        self.__created_by = created_by

    @property
    def updated_at(self) -> Date:
        return self.__updated_at

    @updated_at.setter
    def updated_at(self, updated_at: Date) -> None:
        self.__updated_at = updated_at

    @property
    def updated_by(self) -> ObjectId:
        return self.__updated_by

    @updated_by.setter
    def updated_by(self, updated_by: ObjectId) -> None:
        self.__updated_by = updated_by

    @property
    def deleted_at(self) -> Date:
        return self.__deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at: Date) -> None:
        self.__deleted_at = deleted_at

    @property
    def deleted_by(self) -> ObjectId:
        return self.__deleted_by

    @deleted_by.setter
    def deleted_by(self, deleted_by: ObjectId) -> None:
        self.__deleted_by = deleted_by
