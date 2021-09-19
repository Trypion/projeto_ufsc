from datetime import datetime
from src.models.user import User
from src.models.course import Course
from src.models.university import University
from uuid import uuid4

from src.DAO.profile import ProfileDAO
from bson import ObjectId

from src.controllers.controller import Controller
from src.models.profile import Profile
from src.controllers.errors.profile_not_found import ProfileNotFound


class ProfileController(Controller):
    def __init__(self, profile_dao: ProfileDAO) -> None:
        self.__profile_dao = profile_dao

    def create(self, name: str, email: str, sex: str, age: int, university: ObjectId, profile_picture: str, university_register: str, course: ObjectId, user: ObjectId):

        id = ObjectId()
        created_at = datetime.now()
        profile = Profile(id, name, email, sex, age, university,
                          university_register, course, user, user, created_at, profile_picture)
        self.__profile_dao.save(profile)
        return {'id': str(id)}

    def find(self, id) -> Profile:
        profile = self.find_by_id(id)
        if profile:
            return profile.as_dict()

        raise ProfileNotFound(f"Profile {id} not found")

    def update(self, id: str, name: str, email: str, sex: str, age: int, university: University, profile_picture: str, university_register: str, course: Course, user):
        profile = self.find_by_id(id)
        if not profile:
            return
        profile.name = name
        profile.email = email
        profile.sex = sex
        profile.university = university
        profile.profile_picture = profile_picture
        profile.university_register = university_register
        profile.course = course
        profile.updated_by = user
        profile.age = age
        self.__profile_dao.save(profile)
        return profile.as_dict()

    def delete(self, id: str, user: User) -> str:
        profile = self.find_by_id(id)
        if not profile:
            return
        profile.deleted_by = user
        profile.deleted_at = datetime.now()
        return profile.id

    def find_all(self):
        return [profile.as_dict() for profile in self.__profile_dao.find_all()]

    def find_by_user_id(self, id: str) -> Profile:
        return self.__profile_dao.find_by_user_id(id).as_dict()

    def find_by_id(self, id: str) -> Profile:
        profile = self.__profile_dao.find_by_id(id)
        if not profile:
            raise ProfileNotFound(f"university {id} not found")
        return profile
