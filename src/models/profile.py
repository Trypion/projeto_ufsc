from datetime import datetime

from src.models.course import Course
from src.models.timestamp import Timestamp
from src.models.university import University
from src.models.user import User


class Profile(Timestamp):
    def __init__(self, id: str, name: str, email: str, sex: str, age: int, university: University, profile_picture: str, university_register: str, course: Course, ranking: int, user: User) -> None:
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
        self.__ranking = ranking
        self.__user = user
        self.created_by = user
        self.created_at = datetime.now()


    def as_dict(self):
        return {
            'id': self.__id,
            'name': self.__name,
            'email': self.__email,
            'sex': self.__sex,
            'age': self.__age,
            'university': self.__university.as_dict(),
            'profile_picture': self.__profile_picture,
            'university_register': self.__university_register,
            'course': self.__course.as_dict(),
            'ranking': self.__ranking,
            'user': self.__user.as_dict(),
            'created_by': self.created_by.as_dict(),
            'created_at': datetime.strftime(self.created_at, "%d/%m/%Y"),
            'updated_by': self.updated_by.as_dict() if self.updated_by else None,
            'updated_at': datetime.strftime(self.updated_at, "%d/%m/%Y") if self.updated_at else None,
            'deleted_by': self.deleted_by.as_dict() if self.deleted_by else None,
            'deleted_at': datetime.strftime(self.deleted_at, "%d/%m/%Y") if self.deleted_at else None,
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
