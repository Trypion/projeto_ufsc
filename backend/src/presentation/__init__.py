from flask import request
from flask.helpers import make_response
from flask.json import jsonify
from jsonschema.exceptions import ValidationError
from app import app


from src.utils import helper


from src.DAO.connection import Connection
from src.DAO.user import UserDAO



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
==//DAO//==
'''
dbConnection = Connection().create_connection(app.config['CONNECTION_URI'], app.config['DATABASE'])
userDao = UserDAO(dbConnection)


'''
==//CONTROLLERS//==
'''
user_controlller = UserController(userDao)
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

'''
==//USER//==
'''
@app.route('/api/v1/user/<id>', methods=['GET', 'PUT', 'DELETE'])
@helper.token_required
def user(id, user):
  if request.method == 'GET':
    return jsonify(user_routes.find(id))
  if request.method == 'DELETE':
    return user_routes.delete(id, user), 204
  if request.method == 'PUT':
    return jsonify(user_routes.change_password(request, id, user))
    
