from datetime import datetime
from src.DAO.course import CourseDAO
from src.controllers.controller import Controller
from src.controllers.errors.course_not_found import CourseNotFound
from src.models.course import Course
from src.models.user import User
from bson.objectid import ObjectId


class CourseController(Controller):
    def __init__(self, course_dao: CourseDAO) -> None:
        self.__course_dao = course_dao

    def create(self, name: str, university: ObjectId, created_by: ObjectId):        
        id = ObjectId()
        created_at = datetime.now()
        course = Course(id, name, university, created_by, created_at)
        self.__course_dao.save(course)
        return {'id': str(id)}

    def find(self, id: str) -> dict:
        course = self.find_by_id(id)
        if course:
            return course.as_dict()

    def find_by_university_id(self, id) -> list:
        return [course.as_dict() for course in self.__course_dao.find_by_university_id(id)]

    def find_all(self) -> list:
        return [course.as_dict() for course in self.__course_dao.find_all()]

    def update(self, id: str, name: str, university: ObjectId, user: ObjectId) -> dict:
        course = self.find_by_id(id)
        if not course:
            return
        course.name = name
        course.university = university        
        course.updated_by = user
        course.updated_at = datetime.now()

        self.__course_dao.save(course)

        return course.as_dict()

    def delete(self, id: str, user: User) -> str:
        course = self.find_by_id(id)
        if not course:
            return
        course.deleted_by = user
        course.deleted_at = datetime.now()
        return course.id

    def find_by_id(self, id: str) -> Course:
        course = self.__course_dao.find_by_id(id)
        if not course:
            raise CourseNotFound(f"course {id} not found")

        return course
