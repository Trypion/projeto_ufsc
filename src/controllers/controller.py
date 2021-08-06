from abc import ABC, abstractclassmethod

class Controller(ABC):
    @abstractclassmethod
    def create(self):
        ...

    @abstractclassmethod
    def find(self):
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

