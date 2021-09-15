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
        'password': str(user.password),
        'updatedBy': user.updated_by.as_dict(),
        'updatedAt': user.updated_at
      }
    }

    self.__collection.update_one({'_id': ObjectId(user.id)}, update)
    return user

  
  def findById(self, id: str):
    return self.__collection.find_one(ObjectId(id))
    