from datetime import datetime
from bson import ObjectId
from pymongo.database import Database

from src.models.user import User


class UserDAO():
    def __init__(self, db_conection: Database) -> None:
        self.__collection = db_conection.users

    def save(self, user: User) -> User:
        persisted_user = self.find_by_id(user.id)

        if not persisted_user:
            self.__collection.insert_one(user.serialize())
            return user

        update = {
            '$set': {
                'password': user.password,
                'updated_by': user.updated_by,
                'updated_at': datetime.now(),
                'deleted_at': user.deleted_at,
                'deleted_by': user.deleted_by
            }
        }

        self.__collection.update_one({'_id': ObjectId(user.id)}, update)
        return user

    def find_by_id(self, id: str) -> User:
        user = self.__collection.find_one({'_id': ObjectId(id)})
        if user:
            return self.__deserialize(*user.values())
        return None

    def find_by_login(self, login: str) -> User:
        user = self.__collection.find_one({'login': login, 'deleted_at': None})
        if user:
            return self.__deserialize(*user.values())
        return None

    def __deserialize(self, id, login, password, created_at, updated_by, updated_at, deleted_at, deleted_by):
        return User(id, login, password, created_at, updated_by, updated_at, deleted_at, deleted_by)
