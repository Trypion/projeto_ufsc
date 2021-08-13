from src.controllers.user import UserController
from src.controllers.event import EventController
from src.controllers.university import UniversityController
from flask import Blueprint, json, request
from flask.templating import render_template
from flask_expects_json import expects_json

from src.controllers.profile import ProfileController

class EventRoutes(Blueprint):
    def __init__(self, controller: EventController, user_controller: UserController):
        self.__controller = controller
        self.__user_controller = user_controller
        
        super().__init__('event_bp', __name__)

        # validar JSON
        schema = {
            'type': 'object',
            'properties': {
                'name': {'type': 'string'},
                'start_at': {'type': 'string'},
                'end_at': {'type': 'number'},
                'description': {'type': 'string'},
                'event_picture': {'type': 'string'},
                'location': {'type': 'string'},
                'is_valid': {'type': 'string'},
                'reward': {'type': 'number'}                               
            },
            'required': ['name', 'start_at', 'end_at', 'description', 'event_picture', 'location', 'is_valid', 'reward']
            
        }

        @self.route('/')
        def index():
            return render_template("event/index.html", events=self.__controller.find_all(),users=self.__user_controller.find_all())

        
        @self.route('/findAll', methods=['GET'])
        def find_all():
            return json.dumps(self.__controller.find_all())

        # Criando Event
        @self.route('/', methods=['POST'])
        @expects_json(schema)
        def create():
            name = request.json['name']
            start_at = request.json['start_at']
            end_at = request.json['end_at']
            description = request.json['description']
            event_picture = request.json['event_picture']
            location = request.json['location']
            is_valid = request.json['is_valid']
            reward = request.json['reward']

            user_id = request.headers.get('X-On-Behalf-Of')

            user = self.__user_controller.find_by_id(user_id)
            
            return json.dumps(self.__controller.create(name, start_at, end_at, description, event_picture, location, is_valid, reward, user))

        # Procurando Usuario pela ID
        @self.route('/<id>', methods=['GET'])
        def find(id):
            return json.dumps(self.__controller.find(id))

        @self.route('/<id>', methods=['PUT'])
        @expects_json(schema)
        def update(id):
            name = request.json['name']
            start_at = request.json['start_at']
            end_at = request.json['end_at']
            description = request.json['description']
            event_picture = request.json['event_picture']
            location = request.json['location']
            is_valid = request.json['is_valid']
            reward = request.json['reward']

            user_id = request.headers.get('X-On-Behalf-Of')
            user = self.__user_controller.find_by_id(user_id)

            return json.dumps(self.__controller.update(id, name, start_at, end_at, description, event_picture, location, is_valid, reward, user))


        @self.route('/<id>', methods=['DELETE'])        
        def delete(id):
            user_id = request.headers.get('X-On-Behalf-Of')
            user = self.__user_controller.find_by_id(user_id)   
            return json.dumps(self.__controller.delete(id, user))
