# my_lib
import sqlite3

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

    def search(self, query:str, multiple=False):
        results = self.cursor.execute(query)
        if multiple:
            return results.fetchall() # return multiple rows in a list
        return results.fetchone() # return single value


    def create(self):
        query="""CREATE TABLE if not exists users(
                id INTEGER PRIMARY KEY,
                email text NOT NULl unique,
                password VARCHAR(256) not null,
                username text not null
                )"""
        self.run_query(query)

    def close(self):
        self.connection.close()