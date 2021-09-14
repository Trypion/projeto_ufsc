from flask.json import jsonify
from flask_cors import CORS
from flask import Flask


app = Flask(__name__)
app.config.from_object('config')


cors = CORS(app, expose_headers=[
            "Content-Disposition", "Access-Control-Allow-Origin"])


@app.route('/api/ping')
def ping():
    return jsonify('pong')

from src.presentation import *

if __name__ == '__main__':
    app.debug = True
    app.run()
