from pymongo import MongoClient
from pymongo.database import Database


class Connection():
    def __init__(self) -> None:
        ...

    @staticmethod
    def create_connection(url, database) -> Database:
        client = MongoClient(url)
        return client[database]
