from datetime import datetime
from uuid import uuid4

from src.controllers.controller import Controller
from src.controllers.errors.course_not_found import CourseNotFound
from src.controllers.university import UniversityController
from src.models.course import Course
from src.models.user import User


class CourseController(Controller):
    def __init__(self, university_controller: UniversityController) -> None:
        self.__courses = []
        self.__university_controller = university_controller

    def create(self, name: str, university_id: str, user: User, ranking: int = 0):
        university = self.__university_controller.find_by_id(university_id)
        id = str(uuid4())
        course = Course(id, name, university, user, ranking)
        self.__courses.append(course)
        return id

    def find(self, id: str) -> dict:
        course = self.find_by_id(id)
        return course.as_dict()

    def find_all(self) -> list:
        return [course.as_dict() for course in self.__courses if course.deleted_at == None]

    def update(self, id: str, name: str, university_id: str, user: User, ranking: int) -> dict:
        university = self.__university_controller.find(university_id)
        course = self.find_by_id(id)
        course.name = name
        course.university = university
        course.ranking = ranking
        course.updated_by = user
        course.updated_at = str(datetime.now())
        return course.as_dict()

    def delete(self, id: str, user: User) -> str:
        course = self.find_by_id(id)
        course.deleted_by = user
        course.deleted_at = str(datetime.now())
        return course.id

    def find_by_id(self, id: str) -> Course:
        for course in self.__courses:
            if course.id == id and course.deleted_at == None:
                return course
        raise CourseNotFound(f"course {id} not found")
