from flask import request
from flask.helpers import make_response
from jsonschema.exceptions import ValidationError
from src.presentation import app

from src.utils import helper

'''
==//CONTROLLERS//==
'''
from src.controllers.course import CourseController
from src.controllers.university import UniversityController
from src.controllers.user import UserController
from src.controllers.profile import ProfileController
from src.controllers.event import EventController

'''
==//ROUTES//==
'''
from src.presentation.routes.university import UniversityRoutes
from src.presentation.routes.course import CourseRoutes
from src.presentation.routes.user import UserRoutes
from src.presentation.routes.profile import ProfileRoutes
from src.presentation.routes.event import EventRoutes

'''
==//CONTROLLERS//==
'''
user_controlller = UserController()
university_controlller = UniversityController()
course_controlller = CourseController()
profile_controller = ProfileController()
event_controller = EventController()

'''
==//ROUTES//==
'''
course_routes = CourseRoutes(course_controlller, university_controlller, user_controlller)
university_routes = UniversityRoutes(university_controlller, user_controlller)
user_routes = UserRoutes(user_controlller, app.config['SECRET_KEY'])
profile_routes = ProfileRoutes(profile_controller, university_controlller, course_controlller, user_controlller)
event_routes = EventRoutes(event_controller, user_controlller)

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
==//TEST//==
'''
@app.route('/ping')
def ping():
    return "pong"


'''
==//AUTH//==
'''
@app.route('/v1/login', methods=['POST'])
def login():
  return make_response(user_routes.login(request), 200)

'''
==//REGISTER USER//==
'''
@app.route('/v1/user', methods=['POST'])
def create_user():
  return make_response(user_routes.create(request), 200)

'''
==//USER//==
'''
@app.route('/v1/user/<id>', methods=['GET', 'PUT', 'DELETE'])
@helper.token_required
def user(id, user):
  if request.method == 'GET':
    return make_response(user_routes.find(id), 200)
  if request.method == 'DELETE':
    return make_response(user_routes.delete(id, user), 200)
  if request.method == 'PUT':
    return make_response(user_routes.change_password(request, id, user), 200)
    
