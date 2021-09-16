from flask import json
from flask_expects_json import expects_json
from datetime import datetime, timedelta

import jwt

from src.controllers.user import UserController


class UserRoutes():
    schema = {
        'type': 'object',
        'properties': {
            'login': {'type': 'string'},
            'password': {'type': 'string'}
        },
        'required': ['login', 'password']
    }

    schema_update = {
        'type': 'object',
        'properties': {
            'login': {'type': 'string'},
            'password': {'type': 'string'},
            'new_password': {'type': 'string'},
        },
        'required': ['password', 'new_password']
    }

    def __init__(self, controller: UserController, secret):
        self.__secret = secret
        self.__controller = controller

    def find_all(self):
        return self.__controller.find_all()

    @expects_json(schema)
    def create(self, request):
        login = request.json['login']
        password = request.json['password']
        return {'id': self.__controller.create(login, password)}

    def find(self, id: str):
        return self.__controller.find(id)

    @expects_json(schema_update)
    def change_password(self, request):   
        login = request.json['login']
        password = request.json['password']
        new_password = request.json['new_password']
        return self.__controller.change_password(login, password, new_password)

    def delete(self, id: str, user: str):        
        req_user = self.__controller.find_by_id(user)
        return self.__controller.delete(id, req_user)

    @expects_json(schema)
    def login(self, request):
        login = request.json['login']
        password = request.json['password']
        user_id = self.__controller.login(login, password)
        try:
            payload = {
                'exp': datetime.utcnow() + timedelta(days=0, hours=8),
                'iat': datetime.utcnow(),
                'user_id': str(user_id)
            }
            return {'token': jwt.encode(
                payload,
                self.__secret,
                algorithm='HS256'
            )}
        except Exception as e:
            return e