from datetime import datetime
from pymongo.database import Database
from pymongo.message import update
from src.models.university import University
from bson import ObjectId
class UniversityDAO():
    def __init__(self, db_conection: Database):
        self.__collection = db_conection['university']

    def save(self, university: University):
        persisted_university = self.find_by_id(university.id)

        if not persisted_university:
            self.__collection.insert_one(university.as_dict())
            return university
        
        update = {'$set' : 
            {
            'name' : university.name,
            'uf' : university.uf,
            'updated_by' : university.updated_by,
            'updated_at' : datetime.now(),
            'deleted_by' : university.deleted_by,
            'deleted_at' : university.deleted_at
            }
        }

        self.__collection.update_one({'_id' : ObjectId(university.id)}, update)
        return university

    def find_by_id(self, id: str):
        university = self.__collection.find_one({'_id' : ObjectId(id)})
        if university:
            return University(*university.values())
        
        return None 

