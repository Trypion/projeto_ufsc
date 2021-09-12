from src.controllers.user import UserController
from flask import Blueprint, render_template, request
import datetime
import jwt


class AuthRoutes(Blueprint):
    def __init__(self, user_controller: UserController, config):
        self.config = config
        self.__user_controller = user_controller
        super().__init__('auth_bp', __name__)

        @self.route('/register')
        def register():
            return render_template("auth/register.html")

        @self.route('/login', methods=['POST'])
        def login():
            login = request.json['login']
            password = request.json['password']

            user_id = self.__user_controller.login(login, password)

            try:
                payload = {
                    'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, hours=8),
                    'iat': datetime.datetime.utcnow(),
                    'sub': user_id
                }
                return jwt.encode(
                    payload,
                    config.secret_key,
                    algorithm='HS256'
                )
            except Exception as e:
                return e
            # return render_template("auth/login.html")
