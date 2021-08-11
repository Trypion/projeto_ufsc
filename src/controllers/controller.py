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
