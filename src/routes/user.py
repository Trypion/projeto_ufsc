from flask import Blueprint, json, make_response, request
from flask_expects_json import expects_json
from jsonschema import ValidationError

from src.controllers.user import UserController

class UserRoutes(Blueprint):
    def __init__(self):
        self.__controller = UserController()
        super().__init__('user_bp', __name__)

        #validar JSON
        schema = {
            'type': 'object',
            'properties': {
                'login': {'type': 'string'},
                'password': {'type': 'string'},
            },
            'required': ['login', 'password']
        }

        @self.route('/', methods=['GET'])
        def index():
            return json.dumps(self.__controller.find_all())

        @self.route('/', methods=['POST'])
        @expects_json(schema)
        def create():
            login = request.json['login']
            password = request.json['password']
            return json.dumps(self.__controller.create(login, password))

        @self.route('/<id>', methods=['GET'])
        def find(id):
            return json.dumps(self.__controller.find(id))

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
