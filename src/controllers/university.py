from uuid import uuid4
from datetime import datetime

from src.models.university import University

from src.controllers.controller import Controller

from src.controllers.errors.university_not_found import UniversityNotFound


class UniversityController(Controller):
    __universities = []
    def __init__(self) -> None:
        ...

    def create(self, name: str, uf: str, user: str):
        id = str(uuid4())
        university = University(id, name, uf, user)
        self.__universities.append(university)
        return id

    def find(self, id: str) -> dict:
        university = self.find_by_id(id, self.__universities)
        if (university):
            return university.as_dict

    def find_all(self) -> list:
        return [university.as_dict() for university in self.__universities if university.deleted_at == None]

    def update(self, id, name: str, uf: str, user: str) -> dict:
        university = self.find_by_id(id, self.__universities)
        if not university:
            return
        university.name = name
        university.uf = uf
        university.updated_by = user
        university.updated_at = str(datetime.now())
        return university.as_dict()

    def delete(self, id, user) -> str:
        university = self.find_by_id(id, self.__universities)
        if not university:
            return
        university.deleted_by = user
        university.deleted_at = str(datetime.now())
        return university.id
