from pymongo import MongoClient
from pymongo.database import Database


class Connection():
    def __init__(self) -> None:
        ...

    def create_connection(self, url, database) -> Database:
        client = MongoClient(url)
        return client[database]
