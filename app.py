from flask import Flask, render_template
from flask_cors import CORS

from src.routes.university import UniversityRoutes
from src.routes.user import UserRoutes
from src.routes.auth import AuthRoutes

app = Flask(__name__, template_folder="src/views",
            static_folder="src/views/static")
app.config.from_object('config')

cors = CORS(app, expose_headers=[
            "Content-Disposition", "Access-Control-Allow-Origin"])

university_routes = UniversityRoutes()
user_routes = UserRoutes()
auth_routes = AuthRoutes()

app.register_blueprint(university_routes, url_prefix='/university')
app.register_blueprint(user_routes, url_prefix='/user')
app.register_blueprint(auth_routes, url_prefix='/auth')


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/ping')
def ping():
    return "pong"


if __name__ == '__main__':
    app.debug = True
    app.run()
