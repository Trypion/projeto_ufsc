from flask import Blueprint, json, make_response, request
from flask_expects_json import expects_json
from jsonschema import ValidationError

from src.controllers.user import UserController


class UserRoutes(Blueprint):
    def __init__(self):
        self.__controller = UserController()
        super().__init__('user_bp', __name__)

        # validar JSON
        schema = {
            'type': 'object',
            'properties': {
                'login': {'type': 'string'},
                'password': {'type': 'string'}     
            },
            'required': ['login', 'password']
        }

        schema_update = {
            'type': 'object',
            'properties': { 
                'password': {'type': 'string'},
                'new_password': {'type': 'string'},
                'user': {'type': 'string'}
            },
            'required': ['password', 'new_password', 'user']
        }

        # Retornando todos os usuarios
        @self.route('/', methods=['GET'])
        def index():
            return json.dumps(self.__controller.find_all())

        # Criando Usuario
        @self.route('/', methods=['POST'])
        @expects_json(schema)
        def create():
            login = request.json['login']
            password = request.json['password']
            return json.dumps(self.__controller.create(login, password))

        # Procurando Usuario pela ID
        @self.route('/<id>', methods=['GET'])
        def find(id):
            return json.dumps(self.__controller.find(id))

        @self.route('/<login>', methods=['PUT'])
        @expects_json(schema_update)
        def update(login):
            password = request.json['password']
            new_password = request.json['new_password']
            user = request.json['user']
            return json.dumps(self.__controller.update(login, password, new_password, user))

        @self.route('/<id>', methods=['DELETE'])        
        def delete(id):
            user = request.json['user']    
            return json.dumps(self.__controller.delete(id, user))

        # Mensagens de Erro    
        @self.errorhandler(Exception)
        def handle_exception(error):
            return make_response({"error": str(error)}, 500)

        @self.errorhandler(400)
        def bad_request(error):
            if isinstance(error.description, ValidationError):
                original_error = error.description
                return make_response({'error': original_error.message}, 400)
            # handle other "Bad Request"-errors
            return error
