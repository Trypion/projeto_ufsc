from flask import Blueprint, json, request
from flask.templating import render_template
from flask_expects_json import expects_json

from src.controllers.course import CourseController
from src.controllers.university import UniversityController
from src.controllers.user import UserController


class CourseRoutes(Blueprint):
    def __init__(self, controller: CourseController, university_controller: UniversityController, user_controller: UserController):
        self.__controller = controller
        self.__university_controller = university_controller
        self.__user_controller = user_controller
        super().__init__('course_bp', __name__)

        schema = {
            'type': 'object',
            'properties': {
                'name': {'type': 'string'},
                'university_id': {'type': 'string'},
                'ranking': {'type': 'number'}
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
            user_id = request.headers.get('X-On-Behalf-Of')
            user = self.__user_controller.find_by_id(user_id)
            university = self.__university_controller.find_by_id(university_id)
            return json.dumps(self.__controller.create(name, university, user, ranking))

        @self.route('/<id>', methods=['GET'])
        def find(id):
            return json.dumps(self.__controller.find(id))

        @self.route("/<id>", methods=['PUT'])
        @expects_json(schema)
        def update(id):
            name = request.json['name']
            university_id = request.json['university_id']
            ranking = request.json['ranking']
            user_id = request.headers.get('X-On-Behalf-Of')
            user = self.__user_controller.find_by_id(user_id)
            university = self.__university_controller.find_by_id(university_id)
            return json.dumps(self.__controller.update(id, name, university, user, ranking))

        @self.route("/<id>", methods=['DELETE'])
        def delete(id):
            user_id = request.headers.get('X-On-Behalf-Of')
            user = self.__user_controller.find_by_id(user_id)
            return json.dumps(self.__controller.delete(id, user))

