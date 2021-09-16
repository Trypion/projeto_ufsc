from abc import ABC, abstractclassmethod


class Controller(ABC):
    @abstractclassmethod
    def create(self):
        ...

    @abstractclassmethod
    def find(self):
        '''encontra um objeto e devolve ele em formato de dicionario'''
    
    @abstractclassmethod
    def find_all(self):
        ...

    @abstractclassmethod
    def update(self):
        ...

    @abstractclassmethod
    def delete(self):
        ...
