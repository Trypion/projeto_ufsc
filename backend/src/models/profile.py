from datetime import datetime
from bson import ObjectId
from src.models.timestamp import Timestamp


class Profile(Timestamp):
    def __init__(self, id: str, name: str, email: str, sex: str, age: int, university: ObjectId, university_register: str, course: ObjectId, user: ObjectId, created_by: ObjectId, created_at: datetime, updated_by: ObjectId = None, updated_at: datetime = None, deleted_by: ObjectId = None, deleted_at: datetime = None, profile_picture: str = None) -> None:
        super().__init__()
        self.__id = id
        self.__name = name
        self.__email = email
        self.__sex = sex
        self.__age = age
        self.__university = university
        self.__profile_picture = profile_picture
        self.__university_register = university_register
        self.__course = course
        self.__user = user
        self.created_at = created_at
        self.created_by = created_by
        self.updated_by = updated_by
        self.updated_at = updated_at
        self.deleted_by = deleted_by
        self.deleted_at = deleted_at
    
    def serialize(self):
        return {
            '_id': self.__id,
            'name': self.__name,
            'email': self.__email,
            'sex': self.__sex,
            'age': self.__age,
            'university': self.__university,
            'profile_picture': self.__profile_picture,
            'university_register': self.__university_register,
            'course': self.__course,
            'user': self.__user,
            'created_by': self.created_by,
            'created_at': self.created_at,
            'updated_by': self.updated_by,
            'updated_at': self.updated_at,
            'deleted_by': self.deleted_by,
            'deleted_at': self.deleted_at
        }


    def as_dict(self):
        return {
            'id': self.__id,
            'name': self.__name,
            'email': self.__email,
            'sex': self.__sex,
            'age': self.__age,
            'university': self.__university,
            'profile_picture': self.__profile_picture,
            'university_register': self.__university_register,
            'course': self.__course,
            'user': self.__user,
            'created_by': str(self.created_by),
            'created_at': self.created_at,
            'updated_by': str(self.updated_by),
            'updated_at': self.updated_at,
            'deleted_by': str(self.deleted_by),
            'deleted_at': self.deleted_at
        }

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def sex(self):
        return self.__sex

    @sex.setter
    def sex(self, sex):
        self.__sex = sex

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def university(self):
        return self.__university

    @university.setter
    def university(self, university):
        self.__university = university

    @property
    def profile_picture(self):
        return self.__profile_picture

    @profile_picture.setter
    def profile_picture(self, profile_picture):
        self.__profile_picture = profile_picture

    @property
    def university_register(self):
        return self.__university_register

    @university_register.setter
    def university_register(self, university_register):
        self.__university_register = university_register

    @property
    def course(self):
        return self.__course

    @course.setter
    def course(self, course):
        self.__course = course
        
    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, user):
        self.__user = user
