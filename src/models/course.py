from src.models.university import University
from src.models.timestamp import Timestamp
from datetime import datetime


class Course(Timestamp):
    def __init__(self, id: str, name: str, university_id: str, user: str, ranking: int = 0) -> None:
        super().__init__()
        self.__id = id
        self.__name = name
        self.__university_id = university_id
        self.__ranking = ranking
        self.created_at = datetime.now()
        self.created_by = user

    def as_dict(self):
        return {
            'id': self.__id,
            'name': self.__name,
            'university_id': self.__university_id,
            'ranking': self.__ranking,
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
    def university_id(self) -> str:
        return self.__university_id

    @university_id.setter
    def university_id(self, university_id: str):
        self.__university_id = university_id

    @property
    def ranking(self) -> int:
        return self.__ranking

    @ranking.setter
    def ranking(self, ranking: int) -> None:
        self.__ranking = ranking
