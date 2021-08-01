from flask import Flask
from flask_cors import CORS
from src.routes.university import UniversityRoutes

app = Flask(__name__)
app.config.from_object('config')

cors = CORS(app, expose_headers=[
            "Content-Disposition", "Access-Control-Allow-Origin"])

university_routes = UniversityRoutes()
app.register_blueprint(university_routes, url_prefix='/university')


@app.route('/')
def index():
    return "Home Page"


@app.route('/ping')
def ping():
    return "pong"


if __name__ == '__main__':
    app.debug = True
    app.run()
