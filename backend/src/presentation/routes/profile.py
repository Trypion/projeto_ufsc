from src.controllers.user import UserController
from src.controllers.course import CourseController
from src.controllers.university import UniversityController
from flask import json, request
from flask.templating import render_template
import jwt

from src.controllers.profile import ProfileController


class ProfileRoutes():

    schema = {
        'type': 'object',
        'properties': {
            'name': {'type': 'string'},
            'email': {'type': 'string'},
            'sex': {'type': 'string'},
            'age': {'type': 'number'},
            'university_id': {'type': 'string'},
            'profile_picture': {'type': 'string'},
            'university_register': {'type': 'string'},
            'course_id': {'type': 'string'},
            'ranking': {'type': 'number'}
        },
        'required': ['name', 'email', 'sex', 'age', 'university_id', 'profile_picture', 'university_register', 'course_id', 'ranking']
    }

    def __init__(self, controller: ProfileController, university_controller: UniversityController, course_controller: CourseController, user_controller: UserController):
        self.__controller = controller
        self.__university_controller = university_controller
        self.__course_controller = course_controller
        self.__user_controller = user_controller
        

        # validar JSON

   
   # def find_all():
    #    return self.__controller.find_all()

    # Criando Profile

    def create(self, request, user_id):
        name = request.json['name']
        email = request.json['email']
        sex = request.json['sex']
        age = request.json['age']
        university_id = request.json['university_id']
        profile_picture = request.json['profile_picture']
        university_register = request.json['university_register']
        course_id = request.json['course_id']
        ranking = request.json['ranking']
        user = self.__user_controller.find_by_id(user_id)
        university = self.__university_controller.find_by_id(university_id)            
        course = self.__course_controller.find_by_id(course_id)
        
        return self.__controller.create(name, email, sex, age, university, profile_picture, university_register, course, ranking, user)

    # Procurando Usuario pela ID
    def find(self,id):
        return self.__controller.find(id)

    def update(self, request, id, user_id):
        name = request.json['name']
        email = request.json['email']
        sex = request.json['sex']
        university_id = request.json['university_id']
        profile_picture = request.json['profile_picture']
        university_register = request.json['university_register']
        course_id = request.json['course_id']
        ranking = request.json['ranking']
        user = self.__user_controller.find_by_id(user_id)
        university = self.__university_controller.find_by_id(university_id)            
        course = self.__course_controller.find_by_id(course_id)

        return self.__controller.update(id, name, email, sex,university,profile_picture,university_register, course, ranking, user)

       
    def delete(self, id, user_id):
        user = self.__user_controller.find_by_id(user_id)   
        return self.__controller.delete(id, user)
