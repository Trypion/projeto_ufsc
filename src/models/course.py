from src.models.university import University
from src.models.timestamp import Timestamp
from src.models.user import User

from datetime import datetime


class Course(Timestamp):
    def __init__(self, id: str, name: str, university: University, user: User, ranking: int = 0) -> None:
        super().__init__()
        self.__id = id
        self.__name = name
        self.__university = university
        self.__ranking = ranking
        self.created_at = str(datetime.now())
        self.created_by = user

    def as_dict(self):
        return {
            'id': self.__id,
            'name': self.__name,
            'university_id': self.__university.id,
            'ranking': self.__ranking,
            'created_by': self.created_by.login,
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
    def university(self) -> University:
        return self.__university

    @university.setter
    def university(self, university: University):
        self.__university = university

    @property
    def ranking(self) -> int:
        return self.__ranking

    @ranking.setter
    def ranking(self, ranking: int) -> None:
        self.__ranking = ranking
