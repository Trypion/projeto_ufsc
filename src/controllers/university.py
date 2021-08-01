from src.models.university import University
from uuid import uuid4


class UniversityController():
    def __init__(self) -> None:
        self.__universities = []

    def create(self, name: str, uf: str, user: str):
        id = str(uuid4())
        university = University(id, name, uf, user)
        self.__universities.append(university)
        return id

    def find(self, id: str) -> University:
        for university in self.__universities:
            if university.id == id:
                return university.as_dict()
        return None

    def find_all(self) -> list:
        return [university.as_dict() for university in self.__universities]

    def __check_duplicates(self, list: list, id: str):
        ...
