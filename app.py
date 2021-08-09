from re import S
from flask import Flask, render_template
from flask_cors import CORS

'''controladores'''
from src.controllers.course import CourseController
from src.controllers.university import UniversityController
from src.controllers.user import UserController


'''rotas'''
from src.routes.university import UniversityRoutes
from src.routes.course import CourseRoutes
from src.routes.user import UserRoutes
from src.routes.auth import AuthRoutes

app = Flask(__name__, template_folder="src/views",
            static_folder="src/views/static")
app.config.from_object('config')

cors = CORS(app, expose_headers=[
            "Content-Disposition", "Access-Control-Allow-Origin"])

'''controladores'''
user_controlller = UserController()
university_controlller = UniversityController(user_controlller)
course_controlller = CourseController(university_controlller, user_controlller)

'''rotas'''
course_routes = CourseRoutes(course_controlller, university_controlller, user_controlller)
university_routes = UniversityRoutes(university_controlller, user_controlller)
user_routes = UserRoutes(user_controlller)
auth_routes = AuthRoutes()

app.register_blueprint(university_routes, url_prefix='/university')
app.register_blueprint(course_routes, url_prefix='/course')
app.register_blueprint(user_routes, url_prefix='/user')
app.register_blueprint(auth_routes, url_prefix='/auth')


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/ping')
def ping():
    return "pong"


def seed():
    from src.models.university import University
    from src.models.user import User

    university_seed = [
        {
            "id": "6897958e-a97a-4b07-94aa-e62d56d9d26f",
            "name": "UFSC",
            "uf": "SC",
        },
        {
            "id": "5855a4cb-bcb3-4946-9976-0e041b0690fd",
            "name": "USP",
            "uf": "SP"
        }
    ]
    for university in university_seed:
        university_routes._UniversityRoutes__controller._UniversityController__universities.append(University(
            university['id'], university['name'], university['uf'], '05f92ee5-7bd5-449f-b07d-15705064e08f'))

    user_seed = [
        {
            "id": "05f92ee5-7bd5-449f-b07d-15705064e08f",
            "login": "Israel",
            "password": "12345",
        },
        {
            "id": "f3737123-bf6c-4952-996b-8ef4a52ca9d3",
            "login": "Lissandro",
            "password": "12345",
        }
    ]
    for user in user_seed:
        user_routes._UserRoutes__controller._UserController__users.append(User(
            user['id'], user['login'], user['password']))

if __name__ == '__main__':
    app.debug = True
    seed()
    app.run()
