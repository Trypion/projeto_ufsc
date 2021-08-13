from datetime import datetime
from src.models.event import Event
from src.models.user import User
from src.models.course import Course
from src.models.university import University
from uuid import uuid4

from src.controllers.controller import Controller
from src.models.profile import Profile
from src.controllers.errors.profile_not_found import ProfileNotFound


class ProfileController(Controller):
    def __init__(self) -> None:
        self.__profiles = []

    def create(self, name: str,start_at: str, end_at: str, description: str, event_picture: str, location: str, is_valid : bool, reward: int, user: User):

        id = str(uuid4())
        event = Event(name, start_at, end_at, description, event_picture, location, is_valid, reward, user)
        self.__profiles.append(event)
        return id

    def find(self, id) -> Profile:
        profile = self.find_by_id(id)
        if profile:
            return profile.as_dict()

        raise ProfileNotFound(f"Profile {id} not found")

    def update(self, id: str, name: str, email: str, sex: str, university: University, profile_picture: str, university_register: str, course: Course, ranking: int, user: User):
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
        profile.ranking = ranking
        user = user
        profile.updated_at = datetime.now()
        return profile.as_dict()

    def delete(self, id: str, user: User) -> str:
        profile = self.find_by_id(id)
        if not profile:
            return
        profile.deleted_by = user
        profile.deleted_at = datetime.now()
        return profile.id

    def find_all(self):
        return [profile.as_dict() for profile in self.__profiles if profile.deleted_at == None]

    def find_by_id(self, id: str) -> Profile:
        for profile in self.__profiles:
            if profile.id == id and profile.deleted_at == None:
                return profile
        raise ProfileNotFound(f"Profile {id} not found")
