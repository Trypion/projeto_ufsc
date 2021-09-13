from flask import Flask
from flask_cors import CORS


app = Flask(__name__, template_folder="src/views",
            static_folder="src/views/static")
app.config.from_object('config')

cors = CORS(app, expose_headers=[
            "Content-Disposition", "Access-Control-Allow-Origin"])


from src.presentation import index