from src.controllers.user import UserController
from src.controllers.course import CourseController
from src.controllers.university import UniversityController
from flask import Blueprint, json, request
from flask.templating import render_template
from flask_expects_json import expects_json

from src.controllers.profile import ProfileController

class ProfileRoutes(Blueprint):
    def __init__(self, controller: ProfileController, university_controller: UniversityController, course_controller: CourseController, user_controller: UserController):
        self.__controller = controller
        self.__university_controller = university_controller
        self.__course_controller = course_controller
        self.__user_controller = user_controller
        
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
                'ranking': {'type': 'number'}                               
            },
            'required': ['name', 'email', 'sex', 'age', 'university_id', 'profile_picture', 'university_register', 'course_id', 'ranking']
        }

        @self.route('/')
        def index():
            return render_template("profile/index.html", profiles=self.__controller.find_all(),courses=self.__course_controller.find_all(),universities=self.__university_controller.find_all())

        
        @self.route('/findAll', methods=['GET'])
        def find_all():
            return json.dumps(self.__controller.find_all())

        # Criando Profile
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

            user_id = request.headers.get('X-On-Behalf-Of')

            user = self.__user_controller.find_by_id(user_id)
            university = self.__university_controller.find_by_id(university_id)            
            course = self.__course_controller.find_by_id(course_id)
            
            return json.dumps(self.__controller.create(name, email, sex, age, university, profile_picture, university_register, course, ranking, user))

        # Procurando Usuario pela ID
        @self.route('/<id>', methods=['GET'])
        def find(id):
            return json.dumps(self.__controller.find(id))

        @self.route('/<id>', methods=['PUT'])
        @expects_json(schema)
        def update(id):
            name = request.json['name']
            email = request.json['email']
            sex = request.json['sex']
            university_id = request.json['university_id']
            profile_picture = request.json['profile_picture']
            university_register = request.json['university_register']
            course_id = request.json['course_id']
            ranking = request.json['ranking']
            user_id = request.headers.get('X-On-Behalf-Of')
            user = self.__user_controller.find_by_id(user_id)
            university = self.__university_controller.find_by_id(university_id)            
            course = self.__course_controller.find_by_id(course_id)

            return json.dumps(self.__controller.update(id, name, email, sex,university,profile_picture,university_register, course, ranking, user))


        @self.route('/<id>', methods=['DELETE'])        
        def delete(id):
            user_id = request.headers.get('X-On-Behalf-Of')
            user = self.__user_controller.find_by_id(user_id)   
            return json.dumps(self.__controller.delete(id, user))
