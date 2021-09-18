from datetime import datetime
from src.DAO.course import CourseDAO
from src.models.university import University
from uuid import uuid4
from src.controllers.controller import Controller
from src.controllers.errors.course_not_found import CourseNotFound
from src.models.course import Course
from src.models.user import User
from bson.objectid import ObjectId


class CourseController(Controller):
    def __init__(self, course_dao: CourseDAO) -> None:
        self.__course_dao = course_dao               

    def create(self, name: str, university: University, user: User, created_by: ObjectId, created_at: datetime, updated_by: ObjectId = None, updated_at: datetime = None, deleted_by: ObjectId = None, deleted_at: datetime = None, ranking: int = 0):        
        id = ObjectId()
        course = Course(id, name, university, user, ranking, created_by, updated_by,updated_at,deleted_by,deleted_at, ranking)
        self.__course_dao.save(course)
        return {'id': str(id)}

    def find(self, id: str) -> dict:
        course = self.find_by_id(id)
        return course.as_dict()

    def find_all(self) -> list:
        return [course.as_dict() for course in self.__course_dao.find_all()]

    def update(self, id: str, name: str, university: University, user: User, ranking: int) -> dict:
        course = self.find_by_id(id)
        course.name = name
        course.university = university
        course.ranking = ranking
        course.updated_by = user
        course.updated_at = datetime.now()
        return course.as_dict()

    def delete(self, id: str, user: User) -> str:
        course = self.find_by_id(id)
        course.deleted_by = user
        course.deleted_at = datetime.now()
        return course.id

    def find_by_id(self, id: str) -> Course:
        course = self.__course_dao.find_by_id(id)
        if not course:
            raise CourseNotFound(f"course {id} not found")

        return course
