from flask import Blueprint, json, make_response, request
from flask.templating import render_template
from flask_expects_json import expects_json
from jsonschema import ValidationError

from src.controllers.profile import ProfileController

class ProfileRoutes(Blueprint):
    def __init__(self, controller: ProfileController):
        self.__controller = controller
        super().__init__('profile_bp', __name__)

        # validar JSON
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
                'ranking': {'type': 'number'},
                'user': {'type': 'string'}
                               
            },
            'required': ['name', 'email', 'sex', 'age', 'university_id', 'profile_picture', 'university_register', 'course_id', 'ranking', 'user']
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

        @self.route('/')
        def index():
            return render_template("profile/index.html", users=self.__controller.find_all())

        # Retornando todos os usuarios
        @self.route('/findAll', methods=['GET'])
        def find_all():
            return json.dumps(self.__controller.find_all())

        # Criando Usuario
        @self.route('/', methods=['POST'])
        @expects_json(schema)
        def create():
            name = request.json['name']
            email = request.json['email']
            sex = request.json['sex']
            age = request.json['age']
            university_id = request.json['university_id']
            profile_picture = request.json['profile_picture']
            university_register = request.json['university_register']
            course_id = request.json['course_id']
            ranking = request.json['ranking']
            user = request.json['user']
            
            return json.dumps(self.__controller.create(name, email, sex, age, university_id, profile_picture, university_register, course_id, ranking, user))

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
