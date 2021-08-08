from src.models.timestamp import Timestamp
from datetime import datetime


class Profile(Timestamp):
    def __init__(self, id: str, name: str, email: str, sex: str, age: int, university_id: str, profile_picture: str, university_register: str, course_id: str, ranking: int, user: str) -> None:
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

    def as_dict(self):
        return {
            'id': self.__id,
            'name': self.__name,
            'email': self.__email,
            'sex': self.__sex,
            'age': self.__age,
            'university_id': self.__university_id,
            'profile_picture': self.__profile_picture,
            'university_register': self.__university_register,
            'course_id': self.__course_id,
            'ranking': self.__ranking,
            'user': self.__user,
            'created_at': self.created_at,
            'updated_by': self.updated_by,
            'updated_at': self.updated_at,
            'deleted_by': self.deleted_by,
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
    def university_id(self):
        return self.__university_id

    @university_id.setter
    def university_id(self, university_id):
        self.__university_id = university_id

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
    def course_id(self):
        return self.__course_id

    @course_id.setter
    def course_id(self, course_id):
        self.__course_id = course_id

    @property
    def ranking(self):
        return self.__ranking

    @ranking.setter
    def ranking(self, ranking):
        self.__ranking = ranking

    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, user):
        self.__user = user
