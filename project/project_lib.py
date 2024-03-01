# my_lib
import sqlite3
from passlib.hash import sha256_crypt

hasher = sha256_crypt.using(rounds=30000)

def make_hash(text:str):
    return hasher.hash(text)

def check_hash(hashed_text, text):
    return hasher.verify(text, hashed_text)

class DatabaseWorker:
    def __init__(self, name:str):
        self.name_db = name
        # Step1: Create a connection to the file
        self.connection =  sqlite3.connect(self.name_db)
        self.cursor = self.connection.cursor()

    def run_query(self, query:str):
        self.cursor.execute(query) # run query
        self.connection.commit() # save changes

    def insert(self, query:str):
        self.run_query(query)

    def search(self, query:str, *args, multiple=False):
        results = self.cursor.execute(query, args)
        if multiple:
            return results.fetchall() # return multiple rows in a list
        return results.fetchone() # return single value


    def create(self):
        query="""CREATE TABLE if not exists WORDS(
                id INTEGER PRIMARY KEY,
                length INT,
                word TEXT
                )"""
        self.run_query(query)

    def close(self):
        self.connection.close()