from datetime import datetime
from bson import ObjectId
from pymongo.database import Database
from src.models.course import Course


class CourseDAO():
    def __init__(self, db_conection: Database):
        self.__collection = db_conection['course']

    def save(self, course: Course) -> Course:
        persisted_course = self.find_by_id(course.id)

        if not persisted_course:
            self.__collection.insert_one(course.serialize())
            return course

        update = {
            '$set':
            {
                'id': course.id,
                'name': course.name,
                'university': course.university.as_dict(),
                'ranking': course.ranking,
                'updated_by': course.updated_by,
                'updated_at': datetime.now(),
                'deleted_by': course.deleted_by,
                'deleted_at': course.deleted_at
            }
        }

        self.__collection.update_one({'_id': ObjectId(course.id)}, update)
        return course

    def find_by_id(self, id: str) -> Course:
        course = self.__collection.find_one({'_id': ObjectId(id)})
        if course:
            return self.__deserialize(*course.values())

        return None

    def find_by_university_id(self, id: str):
        documents = self.__collection.find({"university": ObjectId(id)})
        return [self.__deserialize(*document.values()) for document in documents]

    def find_all(self):
        documents = self.__collection.find({'deleted_at': None})
        return [self.__deserialize(*document.values()) for document in documents]

    def __deserialize(self, id, name, university, created_by, created_at, updated_by, updated_at, deleted_by, deleted_at) -> Course:
        return Course(id, name, university, created_by, created_at, updated_by, updated_at, deleted_by, deleted_at)
