from flask import Flask, make_response, render_template
from flask_cors import CORS
from jsonschema import ValidationError

'''controladores'''
from src.controllers.course import CourseController
from src.controllers.university import UniversityController
from src.controllers.user import UserController
from src.controllers.profile import ProfileController
from src.controllers.event import EventController

'''rotas'''
from src.routes.university import UniversityRoutes
from src.routes.course import CourseRoutes
from src.routes.user import UserRoutes
from src.routes.auth import AuthRoutes
from src.routes.profile import ProfileRoutes
from src.routes.event import EventRoutes

app = Flask(__name__, template_folder="src/views",
            static_folder="src/views/static")
app.config.from_object('config')

cors = CORS(app, expose_headers=[
            "Content-Disposition", "Access-Control-Allow-Origin"])

'''controladores'''
user_controlller = UserController()
university_controlller = UniversityController()
course_controlller = CourseController()
profile_controller = ProfileController()
event_controller = EventController()

'''rotas'''
course_routes = CourseRoutes(course_controlller, university_controlller, user_controlller)
university_routes = UniversityRoutes(university_controlller, user_controlller)
user_routes = UserRoutes(user_controlller)
profile_routes = ProfileRoutes(profile_controller, university_controlller, course_controlller, user_controlller)
event_routes = EventRoutes(event_controller, user_controlller)
auth_routes = AuthRoutes()

app.register_blueprint(university_routes, url_prefix='/university')
app.register_blueprint(course_routes, url_prefix='/course')
app.register_blueprint(user_routes, url_prefix='/user')
app.register_blueprint(auth_routes, url_prefix='/auth')
app.register_blueprint(profile_routes, url_prefix='/profile')
app.register_blueprint(event_routes, url_prefix='/event')


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


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/ping')
def ping():
    return "pong"


if __name__ == '__main__':
    app.debug = True
    app.run()