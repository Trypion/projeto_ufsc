from datetime import datetime

from bson import ObjectId
from pymongo.database import Database
from src.models.university import University


class UniversityDAO():
    def __init__(self, db_conection: Database):
        self.__collection = db_conection['university']

    def save(self, university: University) -> University:
        persisted_university = self.find_by_id(university.id)

        if not persisted_university:
            self.__collection.insert_one(university.serialize())
            return university

        update = {
            '$set':
            {
                'name': university.name,
                'uf': university.uf,
                'updated_by': university.updated_by,
                'updated_at': datetime.now(),
                'deleted_by': university.deleted_by,
                'deleted_at': university.deleted_at
            }
        }

        self.__collection.update_one({'_id': ObjectId(university.id)}, update)
        return university

    def find_by_id(self, id: str) -> University:
        university = self.__collection.find_one({'_id': ObjectId(id)})
        if university:
            return self.__deserialize(*university.values())

        return None

    def find_all(self):
        documents = self.__collection.find({'deleted_at': None})
        return [self.__deserialize(*document.values()) for document in documents]

    def __deserialize(self, id, name, uf, created_by, created_at, updated_by, updated_at, deleted_by, deleted_at) -> University:
        return University(id, name, uf, created_by, created_at, updated_by, updated_at, deleted_by, deleted_at)
