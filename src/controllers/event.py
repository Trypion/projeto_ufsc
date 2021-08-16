from datetime import datetime
from src.models.event import Event
from src.models.user import User
#from src.models.course import Course
#from src.models.university import University
from uuid import uuid4

from src.controllers.controller import Controller
#from src.models.profile import Profile
from src.controllers.errors.event_not_found import EventNotFound


class EventController(Controller):
    def __init__(self) -> None:
        self.__events = []

    def create(self, name: str, start_at: str, end_at: str, description: str, event_picture: str, location: str, reward: int, user: User, is_valid: bool = False):

        id = str(uuid4())
        event = Event(id, name, start_at, end_at, description, event_picture, location, is_valid, reward, user)
        self.__events.append(event)
        return id

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
        return event.as_dict()

    def delete(self, id: str, user: User) -> str:
        event = self.find_by_id(id)
        if not event:
            return
        event.deleted_by = user
        event.deleted_at = datetime.now()
        return event.id

    def find_all(self):
        return [event.as_dict() for event in self.__events if event.deleted_at == None]

    def find_by_id(self, id: str) -> Event:
        for event in self.__events:
            if event.id == id and event.deleted_at == None:
                return event
        raise EventNotFound(f"Event {id} not found")
