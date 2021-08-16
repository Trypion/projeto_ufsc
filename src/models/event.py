from datetime import datetime

#from src.models.course import Course
from src.models.timestamp import Timestamp
#from src.models.university import University
from src.models.user import User


class Event(Timestamp):
    # def __init__(self, id: str, name: str,start_at: str, end_at: str, description: str, event_picture: str, location: str, staff : list, result : list, is_valid : bool, votes : list, subscription : list, reward: int, user: User) -> None:
    def __init__(self, id: str, name: str,start_at: str, end_at: str, description: str, event_picture: str, location: str, is_valid : bool, reward: int, user: User) -> None:
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
        self.created_by = user
        self.created_at = datetime.now()
        #self.__staff = staff
        #self.__result = result
        #self.__votes = votes
        #self.__subscription = subscription

    def as_dict(self):
        return {
            'id': self.__id,
            'name': self.__name,
            'start_at': datetime.strftime(self.__start_at, "%d/%m/%Y"),          
            'end_at': datetime.strftime(self.__end_at, "%d/%m/%Y"),
            'description': self.__description,
            'event_picture': self.__event_picture,
            'location': self.__location,
            'is_valid': self.__is_valid,
            'reward': self.__reward,
            'created_by': self.created_by.as_dict(),
            'created_at': datetime.strftime(self.created_at, "%d/%m/%Y"),
            'updated_by': self.updated_by.as_dict() if self.updated_by else None,
            'updated_at': datetime.strftime(self.updated_at, "%d/%m/%Y") if self.updated_at else None,
            'deleted_by': self.deleted_by.as_dict() if self.deleted_by else None,
            'deleted_at': datetime.strftime(self.deleted_at, "%d/%m/%Y") if self.deleted_at else None,
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
