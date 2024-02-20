# Quiz 046
![quiz_046.jpg](..%2F..%2Fassets%2Fprompt%2Fquiz_043-050%2Fquiz_046.jpg)
**Fig.1:** prompt for quiz 046

## 1. flow of chart
![evidence_046.png](..%2F..%2Fassets%2Fevidence%2Fevidence_043-050%2Fevidence_046.png)
**Fig.2:** ER diagram of quiz 046

## 2. solution
```.py
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
```

## 3. Proof of work
![evidence_046.png](..%2F..%2Fassets%2Fevidence%2Fevidence_043-050%2Fevidence_046.png)
**Fig.3:** Evidence for quiz 046