from datetime import datetime
from bson import ObjectId
from pymongo.database import Database

from src.models.user import User


class UserDAO():
    def __init__(self, dbConnection: Database) -> None:
        self.__collection = dbConnection.users

    def save(self, user: User):
        persisted_user = self.findById(user.id)

        if not persisted_user:
            self.__collection.insert_one(user.as_dict())
            return user

        update = {
            '$set': {
                'password': user.password,
                'updatedBy': user.updated_by,
                'updatedAt': datetime.now()
            }
        }

        self.__collection.update_one({'_id': ObjectId(user.id)}, update)
        return user

    def findById(self, id: str):
        return self.__collection.find_one(ObjectId(id))

    def findByLogin(self, login: str) -> User:
        user = self.__collection.find_one({'login': login, 'deletedAt': None})
        if user:
            return User(*user.values())
        return None
