from flask import request
from flask.helpers import make_response
from flask.json import jsonify
from jsonschema.exceptions import ValidationError
from app import app


from src.utils import helper

'''
==//DAO//==
'''
from src.DAO.user import UserDAO
from src.DAO.course import CourseDAO
from src.DAO.profile import ProfileDAO
from src.DAO.connection import Connection
from src.DAO.university import UniversityDAO
from src.DAO.event import EventDAO

'''
==//CONTROLLERS//==
'''
from src.controllers.user import UserController
from src.controllers.event import EventController
from src.controllers.course import CourseController
from src.controllers.profile import ProfileController
from src.controllers.university import UniversityController
'''
==//ROUTES//==
'''
from src.presentation.routes.user import UserRoutes
from src.presentation.routes.event import EventRoutes
from src.presentation.routes.course import CourseRoutes
from src.presentation.routes.profile import ProfileRoutes
from src.presentation.routes.university import UniversityRoutes
'''
==//DAO//==
'''
db_conection = Connection().create_connection(app.config['CONNECTION_URI'], app.config['DATABASE'])
user_dao = UserDAO(db_conection)
course_dao = CourseDAO(db_conection)
profile_dao = ProfileDAO(db_conection)
university_dao = UniversityDAO(db_conection)
event_dao = EventDAO(db_conection)


'''
==//CONTROLLERS//==
'''
event_controller = EventController()
course_controlller = CourseController(course_dao)
user_controlller = UserController(user_dao)
profile_controller = ProfileController(profile_dao)
university_controlller = UniversityController(university_dao)

'''
==//ROUTES//==
'''
event_routes = EventRoutes(event_controller, user_controlller)
user_routes = UserRoutes(user_controlller, app.config['SECRET_KEY'])
university_routes = UniversityRoutes(university_controlller, user_controlller)
course_routes = CourseRoutes(course_controlller, university_controlller, user_controlller)
profile_routes = ProfileRoutes(profile_controller, university_controlller, course_controlller, user_controlller)

'''
==//ERROS//==
'''


@app.errorhandler(Exception)
def handle_exception(error):
    print(str(error))
    return make_response({"error": str(error)}, 500)


@app.errorhandler(400)
def bad_request(error):
    if isinstance(error.description, ValidationError):
        original_error = error.description
        return make_response({'error': original_error.message}, 400)
    # handle other "Bad Request"-errors
    return error


'''
==//AUTH//==
'''


@app.route('/api/v1/login', methods=['POST'])
def login():
    return jsonify(user_routes.login(request))


'''
==//REGISTER USER//==
'''


@app.route('/api/v1/user', methods=['POST'])
def create_user():
    return jsonify(user_routes.create(request))


@app.route('/api/v1/change-password', methods=['POST'])
def change_password():
    return user_routes.change_password(request), 204


'''
==//USER//==
'''


@app.route('/api/v1/user/<id>', methods=['GET', 'DELETE'])
@helper.token_required
def user(id, user):
    if request.method == 'GET':
        return jsonify(user_routes.find(id))
    if request.method == 'DELETE':
        return user_routes.delete(id, user), 204


'''
===//PROFILE//==
'''


@app.route('/api/v1/profile', methods=['POST'])
@helper.token_required
def create_profile(user):
    return jsonify(profile_routes.create(request, user))


@app.route('/api/v1/profile/<id>', methods=['GET', 'PUT', 'DELETE'])
@helper.token_required
def profile(id, user):
    if request.method == 'GET':
        return jsonify(profile_routes.find(id))

    if request.method == 'PUT':
        return jsonify(profile_routes.update(request, id, user))

    if request.method == 'DELETE':
        return jsonify(profile_routes.delete(id, user))


'''
===//UNIVERSITY//==
'''

@app.route('/api/v1/university', methods=['GET'])
def get_university():
    return jsonify(university_routes.find_all())


@app.route('/api/v1/university', methods=['POST'])
@helper.token_required
def create_university(user): 
    return jsonify(university_routes.create(request, user))


@app.route('/api/v1/university/<id>', methods=['GET', 'PUT', 'DELETE'])
@helper.token_required
def university(id, user):
    if request.method == 'GET':
        return jsonify(university_routes.find(id))

    if request.method == 'PUT':
        return jsonify(university_routes.update(request, id, user))

    if request.method == 'DELETE':
        return jsonify(university_routes.delete(id, user))


'''
===//COURSE//==
'''

@app.route('/api/v1/course', methods=['GET'])
def get_courses():
    return jsonify(course_routes.find_all())

@app.route('/api/v1/course/<id>/university', methods=['GET'])
def get_courses_by_university(id):
    return jsonify(course_routes.find_by_university_id(id))


@app.route('/api/v1/course', methods=['POST'])
@helper.token_required
def create_course(request, user):
    return jsonify(course_routes.create())


@app.route('/api/v1/profile/<id>', methods=['GET', 'PUT', 'DELETE'])
@helper.token_required
def course(id, user):
    if request.method == 'GET':
        return jsonify(course_routes.find(id))

    if request.method == 'PUT':
        return jsonify(course_routes.update(request, id, user))

    if request.method == 'DELETE':
        return jsonify(course_routes.delete(id, user))


'''
===//EVENT//==
'''


@app.route('/api/v1/event', methods=['POST'])
@helper.token_required
def create_event(user):
    return jsonify(event_routes.create(request, user))


@app.route('/api/v1/profile/<id>', methods=['GET', 'PUT', 'DELETE'])
@helper.token_required
def event(id, user):
    if request.method == 'GET':
        return jsonify(event_routes.find(id))

    if request.method == 'PUT':
        return jsonify(event_routes.update(request, id, user))

    if request.method == 'DELETE':
        return jsonify(event_routes.delete(id, user))
