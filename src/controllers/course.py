from src.controllers.user import UserController
from src.controllers.university import UniversityController
from src.controllers.errors.course_not_found import CourseNotFound
from uuid import uuid4
from datetime import datetime
from src.controllers.controller import Controller

'''models'''
from src.models.course import Course

'''erros'''

'''controladores'''


class CourseController(Controller):
    __courses = []
    def __init__(self) -> None:
        self.__university_controller = UniversityController()
        self.__user_controller = UserController()

    def create(self, name: str, university_id: str, user: str, ranking: int = 0):
        self.__user_controller.find(user)
        self.__university_controller.find(university_id)

        id = str(uuid4())
        course = Course(id, name, university_id, user, ranking)
        self.__courses.append(course)
        return id

    def find(self, id: str) -> dict:
        course = self.find_by_id(id)
        return course.as_dict

    def find_all(self) -> list:
        return [course.as_dict() for course in self.__courses if course.deleted_at == None]

    def update(self, id, name: str, university_id: str, user: str, ranking: int) -> dict:
        self.__user_controller.find(user)
        self.__university_controller.find(university_id)
        course = self.find_by_id(id)
        course.name = name
        course.university_id = university_id
        course.ranking = ranking
        course.updated_by = user
        course.updated_at = str(datetime.now())
        return course.as_dict()

    def delete(self, id, user) -> str:
        self.__user_controller.find(user)
        course = self.find_by_id(id)
        course.deleted_by = user
        course.deleted_at = str(datetime.now())
        return course.id

    def find_by_id(self, id) -> Course:
        for course in self.__courses:
            if course.id == id and course.deleted_at == None:
                return course
        raise CourseNotFound(f"course {id} not found")
