from src.models.user import User
from uuid import uuid4

class UserController():
    def __init__(self) -> None:
        self.__users = []
    
    def create(self, login : str, password : str) -> str :
        id = str(uuid4())
        user =  User(id,login,password)
        self.__users.append(user)
        return id
    
    def find(self, id) -> User:
        for user in self.__users:
            if (user.id == id):
                return user.as_dict()

        return None
    
    def find_all(self) -> list:
        return [user.as_dict() for user in self.__users]
    
    
