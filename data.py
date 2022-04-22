from pymongo import MongoClient
from dotenv import load_dotenv
import certifi
from os import getenv



class MongoDB:
    """ Creating an """
    load_dotenv()

    def __init__(self, database: str):
        self.database = database

    def get_database(self):
        return MongoClient(
            getenv("MONGO_URL"),
            tlsCAFile=certifi.where(),
        )[self.database]

    def get_collection(self, collection):
        return self.get_database()[collection]

    
if (__name__) == '__main__':
    db = MongoDB("UnderdogDevs")
    print(db.get_collection("Mentors"))