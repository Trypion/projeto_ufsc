from datetime import datetime
from src.presentation import event

from bson.objectid import ObjectId
from src.models.event import Event
from src.models.user import User
#from src.models.course import Course
#from src.models.university import University
from uuid import uuid4
from src.DAO.event import EventDAO
from src.controllers.controller import Controller
#from src.models.profile import Profile
from src.controllers.errors.event_not_found import EventNotFound


class EventController(Controller):
    def __init__(self, event_dao: EventDAO) -> None:
        self.__event_dao = event_dao

    def create(self, name: str, start_at: str, end_at: str, description: str, event_picture: str, location: str, reward: int, user: ObjectId, is_valid: bool = False):

        id = ObjectId()
        created_at = datetime.now()
        event = Event(id, name, start_at, end_at, description, event_picture, location, is_valid, reward, user, user, created_at)
        self.__event_dao.save(event)
        return {'id': str(id)}

    def find(self, id) -> Event:
        event = self.find_by_id(id)
        if event:
            return event.as_dict()

        raise EventNotFound(f"Event {id} not found")

    def update(self, id: str, name: str,start_at: str, end_at: str, description: str, event_picture: str, location: str, is_valid : bool, reward: int, user: User):
        event = self.find_by_id(id)
        if not event:
            return
        event.name = name
        event.start_at = start_at
        event.end_at = end_at
        event.description = description
        event.event_picture = event_picture
        event.location = location
        event.is_valid = is_valid
        event.reward = reward
        event.updated_by = user
        event.updated_at = datetime.now()
        self.__event_dao.save(event)
        return event.as_dict()

    def delete(self, id: str, user: User) -> str:
        event = self.find_by_id(id)
        if not event:
            return
        event.deleted_by = user
        event.deleted_at = datetime.now()
        return event.id

    def find_all(self):
        return [event.as_dict() for event in self.__event_dao.find_all()]

    def find_by_id(self, id: str) -> Event:
        event = self.__event_dao.find_by_id(id)
        if not event:
            raise EventNotFound(f"Event {id} not found")
        return event
        
