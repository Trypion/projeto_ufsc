from datetime import datetime
from src.controllers.user import UserController
from src.controllers.event import EventController
from src.controllers.university import UniversityController
from flask import json, request
#from flask.templating import render_template
from flask_expects_json import expects_json

from src.controllers.profile import ProfileController


class EventRoutes():

    schema = {
        'type': 'object',
        'properties': {
            'name': {'type': 'string'},
            'start_at': {'type': 'string'},
            'end_at': {'type': 'string'},
            'description': {'type': 'string'},
            'event_picture': {'type': 'string'},
            'location': {'type': 'string'},
            'reward': {'type': 'number'}
        },
        'required': ['name', 'start_at', 'end_at', 'description', 'event_picture', 'location', 'reward']
    }

    def __init__(self, controller: EventController, user_controller: UserController):
        self.__controller = controller
        self.__user_controller = user_controller

    def find_all(self):
        return self.__controller.find_all()

    def search(self, request: request):
        start_at = datetime.strptime(request.args.get('from'), "%Y-%m-%dT%H:%M:%S.%fZ")  if request.args.get('from') else None
        end_at = datetime.strptime(request.args.get('to'), "%Y-%m-%dT%H:%M:%S.%fZ") if request.args.get('to') else None
        name = request.args.get('name') if request.args.get('name') else None
        return self.__controller.search(start_at, end_at, name)


    # Criando Event
    @expects_json(schema)
    def create(self, request, user_id):
        name = request.json['name']
        start_at = request.json['start_at']
        end_at = request.json['end_at']
        description = request.json['description']
        event_picture = request.json['event_picture']
        location = request.json['location']
        reward = request.json['reward']

        user = self.__user_controller.find_by_id(user_id).id

        return self.__controller.create(name, start_at, end_at, description, event_picture, location, reward, user)

    # Procurando Usuario pela ID
    def find(self, id):
        return self.__controller.find(id)

    @expects_json(schema)
    def update(self, request, id, user_id):
        name = request.json['name']
        start_at = datetime.strptime(request.json['start_at'], "%d/%m/%Y")
        end_at = datetime.strptime(request.json['end_at'], "%d/%m/%Y")
        description = request.json['description']
        event_picture = request.json['event_picture']
        location = request.json['location']
        reward = request.json['reward']

        user = self.__user_controller.find_by_id(user_id)

        return json.dumps(self.__controller.update(id, name, start_at, end_at, description, event_picture, location, False, reward, user))

    def delete(self, id, user_id):
        user = self.__user_controller.find_by_id(user_id)
        return json.dumps(self.__controller.delete(id, user))
