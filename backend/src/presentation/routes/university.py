from flask import json, request
from flask.templating import render_template
from flask_expects_json import expects_json

from src.controllers.university import UniversityController
from src.controllers.user import UserController


class UniversityRoutes():

    schema = {
    'type': 'object',
    'properties': {
        'name': {'type': 'string'},
        'uf': {'type': 'string'}
    },
    'required': ['name', 'uf']
    
    }

    def __init__(self, controller: UniversityController, user_controller: UserController):
        self.__controller = controller
        self.__user_controller = user_controller

    @self.route('/')
    def index(self):
        return render_template("university/index.html", universities=self.__controller.find_all())

    #@self.route('/findAll', methods=['GET'])
    #def find_all():
    #    return json.dumps(self.__controller.find_all())

    @expects_json(schema)
    def create(self, request, user_id):
        name = request.json['name']
        uf = request.json['uf']
        user = self.__user_controller.find_by_id(user_id)
        return json.dumps(self.__controller.create(name, uf, user))

    def find(self, id):
        return json.dumps(self.__controller.find(id))

    @expects_json(schema)
    def update(self, request, id, user_id):
        name = request.json['name']
        uf = request.json['uf']
        user = self.__user_controller.find_by_id(user_id)
        return json.dumps(self.__controller.update(id, name, uf, user))

    def delete(self, id, user_id):
        user = self.__user_controller.find_by_id(user_id)
        return json.dumps(self.__controller.delete(id, user))
