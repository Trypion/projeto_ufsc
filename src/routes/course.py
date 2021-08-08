from flask import Blueprint, json, make_response, request
from flask.templating import render_template
from flask_expects_json import expects_json
from jsonschema import ValidationError

from src.controllers.course import CourseController
from src.controllers.university import UniversityController


class CourseRoutes(Blueprint):
    def __init__(self):
        self.__controller = CourseController()
        self.__university_controller = UniversityController()
        super().__init__('course_bp', __name__)

        schema = {
            'type': 'object',
            'properties': {
                'name': {'type': 'string'},
                'university_id': {'type': 'string'},
                'ranking': {'type': 'int'}
            },
            'required': ['name', 'university_id', 'ranking']
        }

        @self.route('/')
        def index():
            return render_template("course/index.html", courses=self.__controller.find_all(), universities=self.__university_controller.find_all())

        @self.route('/findAll', methods=['GET'])
        def find_all():
            return json.dumps(self.__controller.find_all())

        @self.route('/', methods=['POST'])
        @expects_json(schema)
        def create():
            name = request.json['name']
            university_id = request.json['university_id']
            ranking = request.json['ranking']
            user = request.headers.get('X-On-Behalf-Of')
            return json.dumps(self.__controller.create(name, university_id, user, ranking))

        @self.route('/<id>', methods=['GET'])
        def find(id):
            return json.dumps(self.__controller.find(id))

        @self.route("/<id>", methods=['PUT'])
        @expects_json(schema)
        def update(id):
            name = request.json['name']
            university_id = request.json['university_id']
            ranking = request.json['ranking']
            user = request.headers.get('X-On-Behalf-Of')
            return json.dumps(self.__controller.update(id, name, university_id, user, ranking))

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
