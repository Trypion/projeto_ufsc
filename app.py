from flask import Flask
from routes.university import UniversityRoutes

app = Flask(__name__)
app.config.from_object('config')

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
