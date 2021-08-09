from src.controllers.errors.controller_not_found import ControllerNotFound

from abc import ABC, abstractclassmethod



class Controller(ABC):
    @abstractclassmethod
    def create(self):
        ...

    @abstractclassmethod
    def find(self, id, ):
        ...

    @abstractclassmethod
    def find_all(self):
        ...

    @abstractclassmethod
    def update(self):
        ...

    @abstractclassmethod
    def delete(self):

        ...

    def find_by_id(self, id, list_object) -> object:
        for find in list_object:
            if find.id == id and find.deleted_at == None:
                return find

        raise ControllerNotFound(f"Object {id} not found")
