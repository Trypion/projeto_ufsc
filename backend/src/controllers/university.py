from bson import ObjectId

from src.controllers.controller import Controller
from src.controllers.errors.university_not_found import UniversityNotFound
from src.models.university import University
from src.models.user import User


class UniversityController(Controller):
    def __init__(self) -> None:        
        ...

    def create(self, name: str, uf: str, user: User):        
        id = ObjectId()
        university = University(id, name, uf, user)
        self.__universities.append(university)   
        return id

    def find(self, id: str) -> dict:
        university = self.find_by_id(id)
        if (university):            
            return university.as_dict()

    def find_all(self) -> list:
        return [university.as_dict() for university in self.__universities if university.deleted_at == None]

    def update(self, id: str, name: str, uf: str, user: str) -> dict:
        university = self.find_by_id(id)
        if not university:
            return
        university.name = name
        university.uf = uf
        university.updated_by = user
        university.updated_at = datetime.now()
        return university.as_dict()

    def delete(self, id: str, user: User) -> str:
        university = self.find_by_id(id)
        if not university:
            return
        university.deleted_by = user
        university.deleted_at = datetime.now()
        return university.id

    def find_by_id(self, id: str) -> University:
        for university in self.__universities:
            if university.id == id and university.deleted_at == None:
                return university
        raise UniversityNotFound(f"university {id} not found")
