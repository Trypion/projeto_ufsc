import json
from flask import Blueprint
from flask.helpers import make_response
from flask import request

from src.controllers.university import UniversityController

# ============================================================================
'''Alternativa a uma classe de rotas'''

# controller = UniversityController()

# university_bp = Blueprint('university_bp', __name__)
# university_bp.route('/', methods=['GET'])(controller.find_all)
# university_bp.route('/create', methods=['POST'])(controller.create)
# university_bp.route('/<id>', methods=['GET'])(controller.find)

# ============================================================================


class UniversityRoutes(Blueprint):
    def __init__(self):
        self.__controller = UniversityController()
        super().__init__('university_bp', __name__)

        @self.route('/', methods=['GET'])
        def index():
            try:
                return json.dumps(self.__controller.find_all())
            except Exception as err:
                return make_response({"error": str(err)}, 500)

        @self.route('/', methods=['POST'])
        def create():
            try:
                name = request.json['name']
                uf = request.json['uf']
                user = request.json['user']
                return json.dumps(self.__controller.create(name, uf, user))
            except Exception as err:
                return make_response({"error": str(err)}, 500)

        @self.route('/<id>', methods=['GET'])
        def find(id):
            try:
                return json.dumps(self.__controller.find(id))
            except Exception as err:
                return make_response({"error": str(err)}, 500)
