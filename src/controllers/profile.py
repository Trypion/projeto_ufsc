from uuid import uuid4
from datetime import datetime
from src.controllers.controller import Controller
from src.models.profile import Profile
from src.controllers.errors.user_not_found import UserNotFound
from src.controllers.user import UserController
from src.controllers.university import UniversityController
from src.controllers.course import CourseController


class ProfileController(Controller):
    def __init__(self, user_controller : UserController, university_controller : UniversityController, course_controller : CourseController) -> None:
        self.__profiles = []
        self.__user_controller = user_controller
        self.__university_controller = university_controller
        self.__course_controller = course_controller

    def create(self, name: str, email: str, sex: str, age: int, university_id: str, profile_picture: str, university_register: str, course_id: str, ranking: int, user : str):
        self.__user_controller.find(user)
        self.__university_controller.find(university_id)
        self.__course_controller.find(course_id)
        
        id = str(uuid4())
        profile = Profile(id, name, email, sex, age, university_id,
                          profile_picture, university_register, course_id, ranking, user)
        self.__profiles.append(profile)
        return id




    def find(self, id) -> Profile:
        for user in self.__profiles:
            if (self.__profiles.id == id and user.deleted_at == None):
                return user.as_dict()

        raise UserNotFound(f"profiles {id} not found")

    def update(self, name: str, email: str, sex: str, university_id: str, profile_picture: str, university_register: str, course_id: str, ranking: int, user: str):
        profile = self.find_by_id(id, self.__profiles)
        if not profile:
            return
        profile.name = name
        profile.email = email
        profile.sex = sex
        profile.university_id = university_id
        profile.profile_picture = profile_picture
        profile.university_register = university_register
        profile.course_id = course_id
        profile.ranking = ranking
        user = user
        profile.updated_at = str(datetime.now())
        return profile.as_dict()

    def delete(self, id, user) -> str:
        profile = self.find_by_id(id)
        if not profile:
            return
        profile.deleted_by = user
        profile.deleted_at = str(datetime.now())
        return profile.id
    
    def find_all(self):
        return [profile.as_dict() for profile in self.__profiles if profile.deleted_at == None]
    

