import sqlite3
from quiz_lib import DatabaseWorker

haiku = """Code flows like astream
Algorithms guide its way
In silence, it solves"""

#Create Database with table Words
db_name = "haiku_db"
db = DatabaseWorker(name=db_name)
# db.create()
# db.close()


# for word in haiku.split():
#     query = f"""INSERT into WORDS (length, word)
#              values ('{len(word)}','{word}')"""
#     db.insert(query=query)

query = f"""SELECT AVG(length) from WORDS"""
out = db.search(query)


print("average world length is", out)