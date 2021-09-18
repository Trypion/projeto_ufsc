from flask import json, request
from flask_expects_json import expects_json

from src.controllers.course import CourseController
from src.controllers.university import UniversityController
from src.controllers.user import UserController


class CourseRoutes():

    schema = {
        'type': 'object',
        'properties': {
                'name': {'type': 'string'},
                'university_id': {'type': 'string'},
                'ranking': {'type': 'number'}
        },
        'required': ['name', 'university_id', 'ranking']
    }

    def __init__(self, controller: CourseController, university_controller: UniversityController, user_controller: UserController):
        self.__controller = controller
        self.__university_controller = university_controller
        self.__user_controller = user_controller

    def find_by_university_id(self, id):
        return self.__controller.find_by_university_id(id)

    def find_all(self):
        return self.__controller.find_all()

    @expects_json(schema)
    def create(self, user_id):
        name = request.json['name']
        university_id = request.json['university_id']
        ranking = request.json['ranking']
        user = self.__user_controller.find_by_id(user_id)
        university = self.__university_controller.find_by_id(university_id)
        return json.dumps(self.__controller.create(name, university, user, ranking))

    @expects_json(schema)
    def find(self, id):
        return json.dumps(self.__controller.find(id))

    @expects_json(schema)
    def update(self, request, id, user_id):
        name = request.json['name']
        university_id = request.json['university_id']
        ranking = request.json['ranking']
        user = self.__user_controller.find_by_id(user_id)
        university = self.__university_controller.find_by_id(university_id)
        return json.dumps(self.__controller.update(id, name, university, user, ranking))

    def delete(self, id, user_id):
        user = self.__user_controller.find_by_id(user_id)
        return json.dumps(self.__controller.delete(id, user))
