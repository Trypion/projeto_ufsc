from src.models.timestamp import Timestamp
from datetime import datetime

class Profile(Timestamp):
    def __init__(self, id : str, name : str, email : str, sex :str, age : str, university_id : str, profile_picture : str, university_register : str, course_id : str, ranking : int, user : str ) -> None:
        super().__init__()
        self.__id = id
        self.__name = name
        self.__email = email
        self.__sex = sex
        self.__age = age
        self.__university_id = university_id
        self.__profile_picture = profile_picture
        self.__university_register = university_register
        self.__course_id = course_id
        self.__ranking = ranking
        self.__user = user
    
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name

