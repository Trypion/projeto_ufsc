from datetime import datetime
from src.models.timestamp import Timestamp
from bson.objectid import ObjectId


class Event(Timestamp):
    def __init__(self, id: str, name: str, start_at: str, end_at: str, description: str, event_picture: str, location: str, is_valid: bool, reward: int, user: ObjectId, created_by: ObjectId, created_at: datetime, updated_by: ObjectId = None, updated_at: datetime = None, deleted_by: ObjectId = None, deleted_at: datetime = None) -> None:
        super().__init__()
        self.__id = id
        self.__name = name
        self.__start_at = start_at
        self.__end_at = end_at
        self.__description = description
        self.__event_picture = event_picture
        self.__location = location
        self.__is_valid = is_valid
        self.__reward = reward
        self.created_at = created_at
        self.created_by = created_by
        self.updated_by = updated_by
        self.updated_at = updated_at
        self.deleted_by = deleted_by
        self.deleted_at = deleted_at

    def serialize(self):
        return {
            '_id': self.__id,
            'name': self.__name,
            'start_at': self.__start_at,
            'end_at': self.__end_at,
            'description': self.__description,
            'event_picture': self.__event_picture,
            'location': self.__location,
            'is_valid': self.__is_valid,
            'reward': self.__reward,
            'created_by': self.created_by,
            'created_at': self.created_at,
            'updated_by': self.updated_by,
            'updated_at': self.updated_at,
            'deleted_by': self.deleted_by,
            'deleted_at': self.deleted_at
        }

    def as_dict(self):
        return {
            'id': str(self.__i),
            'name': self.__name,
            'start_at': self.__start_at,
            'end_at': self.__end_at,
            'description': self.__description,
            'event_picture': self.__event_picture,
            'location': self.__location,
            'is_valid': self.__is_valid,
            'reward': self.__reward,
            'created_by': str(self.created_by),
            'created_at': self.created_at,
            'updated_by': str(self.updated_by),
            'updated_at': self.updated_at,
            'deleted_by': str(self.deleted_by),
            'deleted_at': self.deleted_at
        }

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def start_at(self):
        return self.__start_at

    @start_at.setter
    def start_at(self, start_at):
        self.__start_at = start_at

    @property
    def end_at(self):
        return self.__end_at

    @end_at.setter
    def end_at(self, end_at):
        self.__end_at = end_at

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        self.__description = description

    @property
    def event_picture(self):
        return self.__event_picture

    @event_picture.setter
    def event_picture(self, event_picture):
        self.__event_picture = event_picture

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location):
        self.__location = location

    @property
    def is_valid(self):
        return self.__is_valid

    @is_valid.setter
    def is_valid(self, is_valid):
        self.__is_valid = is_valid

    @property
    def reward(self):
        return self.__reward

    @reward.setter
    def reward(self, reward):
        self.__reward = reward

    @property
    def ranking(self):
        return self.__ranking

    @ranking.setter
    def ranking(self, ranking):
        self.__ranking = ranking
