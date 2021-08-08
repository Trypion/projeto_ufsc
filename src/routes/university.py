from flask import Blueprint, json, make_response, request
from flask.templating import render_template
from flask_expects_json import expects_json
from jsonschema import ValidationError

from src.controllers.university import UniversityController


class UniversityRoutes(Blueprint):
    def __init__(self):
        self.__controller = UniversityController()
        super().__init__('university_bp', __name__)

        schema = {
            'type': 'object',
            'properties': {
                'name': {'type': 'string'},
                'uf': {'type': 'string'}      
            },
            'required': ['name', 'uf']
        }

        @self.route('/')
        def index():
            return render_template("university/index.html", universities=self.__controller.find_all())

        @self.route('/findAll', methods=['GET'])
        def find_all():
            return json.dumps(self.__controller.find_all())

        @self.route('/', methods=['POST'])
        @expects_json(schema)
        def create():
            name = request.json['name']
            uf = request.json['uf']
            user = request.headers.get('X-On-Behalf-Of')
            return json.dumps(self.__controller.create(name, uf, user))

        @self.route('/<id>', methods=['GET'])
        def find(id):
            return json.dumps(self.__controller.find(id))

        @self.route("/<id>", methods=['PUT'])
        @expects_json(schema)
        def update(id):
            name = request.json['name']
            uf = request.json['uf']
            user = request.headers.get('X-On-Behalf-Of')
            return json.dumps(self.__controller.update(id, name, uf, user))

        @self.route("/<id>", methods=['DELETE'])
        def delete(id):
            user = request.headers.get('X-On-Behalf-Of')
            return json.dumps(self.__controller.delete(id, user))

        @self.errorhandler(Exception)
        def handle_exception(error):
            print(str(error))
            return make_response({"error": str(error)}, 500)

        @self.errorhandler(400)
        def bad_request(error):
            if isinstance(error.description, ValidationError):
                original_error = error.description
                return make_response({'error': original_error.message}, 400)
            # handle other "Bad Request"-errors
            return error
