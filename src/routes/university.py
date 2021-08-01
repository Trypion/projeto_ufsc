from flask import Blueprint, json, make_response, request
from flask_expects_json import expects_json
from jsonschema import ValidationError

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

        schema = {
            'type': 'object',
            'properties': {
                'name': {'type': 'string'},
                'uf': {'type': 'string'},
                'user': {'type': 'string'}
            },
            'required': ['name', 'uf', 'user']
        }

        @self.route('/', methods=['GET'])
        def index():
            return json.dumps(self.__controller.find_all())

        @self.route('/', methods=['POST'])
        @expects_json(schema)
        def create():
            name = request.json['name']
            uf = request.json['uf']
            user = request.json['user']
            return json.dumps(self.__controller.create(name, uf, user))

        @self.route('/<id>', methods=['GET'])
        def find(id):
            return json.dumps(self.__controller.find(id))

        @self.errorhandler(Exception)
        def handle_exception(error):
            return make_response({"error": str(error)}, 500)

        @self.errorhandler(400)
        def bad_request(error):
            if isinstance(error.description, ValidationError):
                original_error = error.description
                return make_response({'error': original_error.message}, 400)
            # handle other "Bad Request"-errors
            return error
