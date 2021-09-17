from datetime import datetime
from src.DAO.university import UniversityDAO
from bson import ObjectId

from src.controllers.controller import Controller
from src.controllers.errors.university_not_found import UniversityNotFound
from src.models.university import University
from src.models.user import User


class UniversityController(Controller):
    def __init__(self, university_dao: UniversityDAO) -> None:
        self.__university_dao = university_dao

    def create(self, name: str, uf: str, user: User):
        id = ObjectId()
        created_at = datetime.now()
        university = University(id, name, uf, user, created_at)
        self.__university_dao.save(university)
        return {'id': str(id)}

    def find(self, id: str) -> dict:
        university = self.find_by_id(id)
        if (university):
            return university.as_dict()

    def find_all(self) -> list:
        return [university.as_dict() for university in self.__university_dao.find_all()]

    def update(self, id: str, name: str, uf: str, user: str) -> dict:
        university = self.find_by_id(id)
        if not university:
            return
        university.name = name
        university.uf = uf
        university.updated_by = user

        self.__university_dao.save(university)

        return university.as_dict()

    def delete(self, id: str, user: User) -> str:
        university = self.find_by_id(id)
        if not university:
            return
        university.deleted_by = user
        university.deleted_at = datetime.now()
        return university.id

    def find_by_id(self, id: str) -> University:
        university = self.__university_dao.find_by_id(id)
        if not university:
            raise UniversityNotFound(f"university {id} not found")

        return university
