from datetime import datetime
from bson import ObjectId
from pymongo.database import Database
from src.models.event import Event


class EventDAO():
    def __init__(self, db_conection: Database):
        self.__collection = db_conection['event']

    def save(self, event: Event) -> Event:
        persisted_event = self.find_by_id(event.id)

        if not persisted_event:
            self.__collection.insert_one(event.serialize())
            return event

        update = {
            '$set':
            {
                'id': event.id,
                'name': event.name,
                'start_at': event.start_at,
                'end_at': event.end_at,
                'description': event.description,
                'event_picture': event.event_picture,
                'location': event.location,
                'is_valid': event.is_valid,
                'reward': event.reward,
                'updated_by': event.updated_by,
                'updated_at': datetime.now(),
                'deleted_by': event.deleted_by,
                'deleted_at': event.deleted_at
            }
        }

        self.__collection.update_one({'_id': ObjectId(event.id)}, update)
        return event

    def find_by_id(self, id: str) -> Event:
        event = self.__collection.find_one({'_id': ObjectId(id)})
        if event:
            return self.__deserialize(*event.values())

        return None

    def find_all(self):
        documents = self.__collection.find({'deleted_at': None})
        return [self.__deserialize(*document.values()) for document in documents]

    def __deserialize(self, id, name, start_at, end_at, description, event_picture, location, is_valid, reward, created_by, created_at, updated_by, updated_at, deleted_by, deleted_at) -> Event:
        return Event(id, name, start_at, end_at, description, event_picture, location, is_valid, reward, created_by, created_at, updated_by, updated_at, deleted_by, deleted_at)
