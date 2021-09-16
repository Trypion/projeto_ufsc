from datetime import datetime
from bson import ObjectId
from pymongo.database import Database

from src.models.user import User


class UserDAO():
    def __init__(self, dbConnection: Database) -> None:
        self.__collection = dbConnection.users

    def save(self, user: User) -> User:
        persisted_user = self.find_by_id(user.id)

        if not persisted_user:
            self.__collection.insert_one(user.as_dict())
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
            return User(*user.values())
        return None

    def find_by_login(self, login: str) -> User:
        user = self.__collection.find_one({'login': login, 'deleted_at': None})
        if user:
            return User(*user.values())
        return None
