from datetime import datetime

from bson import ObjectId
from pymongo.database import Database
from src.models.profile import Profile


class ProfileDAO():
    def __init__(self, db_conection: Database):
        self.__collection = db_conection['profile']

    def save(self, profile: Profile) -> Profile:
        persisted_profile = self.find_by_id(profile.id)

        if not persisted_profile:
            self.__collection.insert_one(profile.serialize())
            return profile

        update = {
            '$set':
            {
                'id': profile.id,
                'name': profile.name,
                'email': profile.email,
                'sex': profile.sex,
                'age': profile.age,
                'university': profile.university,
                'profile_picture': profile.profile_picture,
                'university_register': profile.university_register,
                'course': profile.course,
                'ranking': profile.ranking,
                'user': profile.user,
                'updated_by': profile.updated_by,
                'updated_at': datetime.now(),
                'deleted_by': profile.deleted_by,
                'deleted_at': profile.deleted_at
            }
        }

        self.__collection.update_one({'_id': profile.id}, update)
        return profile

    def find_by_id(self, id: str) -> Profile:
        profile : dict = self.__collection.find_one({'_id': ObjectId(id)})
        if profile:
            return self.__deserialize(*profile.values())

        return None

    def find_all(self):
        documents = self.__collection.find({'deleted_at': None})
        return [self.__deserialize(*document.values()) for document in documents]

    def __deserialize(self, id, name, email, sex, age, university, profile_picture, university_register, course, 
    ranking, user, created_by, created_at, updated_by, updated_at, deleted_by, deleted_at) -> Profile:
        return Profile(self, id, name, email, sex, age, university, profile_picture, university_register, course, 
    ranking, user, created_by, created_at, updated_by, updated_at, deleted_by, deleted_at)
