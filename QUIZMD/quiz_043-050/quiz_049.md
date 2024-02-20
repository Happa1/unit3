# Quiz 049
![quiz_diagram_049.jpg](..%2F..%2Fassets%2Fflowchart%2Fflowchart_043-050%2Fquiz_diagram_049.jpg)
**Fig.1:** prompt of quiz num

## 1. flow of chart
![quiz_diagram_049.jpg](..%2F..%2Fassets%2Fflowchart%2Fflowchart_043-050%2Fquiz_diagram_049.jpg)
**Fig.2:** algorithm flow chart of quiz 049

## 2. solution
```.py
from quiz_lib import DatabaseWorker, check_hash

x = DatabaseWorker(name='bitcoin_exchange.db')

# create_user = """CREATE TABLE if not exists users(
# id INTEGER PRIMARY KEY,
# name TEXT,
# email TEXT)"""
#
# x.run_query(create_user)

# insert_query = """INSERT INTO users VALUES
# (560, 'bob1', 'bob1@xyz'),
# (254, 'bob2', 'bob2@xyz'),
# (920, 'bob3', 'bob3@xyz'),
# (438, 'bob4', 'bob4@xyz'),
# (744, 'bob5', 'bob5@xyz'),
# (261, 'bob6', 'bob6@xyz'),
# (371, 'bob7', 'bob7@xyz'),
# (561, 'bob8', 'bob8@xyz'),
# (488, 'bob9', 'bob9@xyz');
# """
#
# x.run_query(insert_query)

sql_query = "SELECT * from ledger"

results = x.search(query=sql_query, multiple=True)

for row in results:
    id = row[0]
    sender_id = row[1]
    receiver_id = row[2]
    amount = row[3]
    signature = row[4]

    hash_text = f"id {id},sender_id {sender_id},receiver_id {receiver_id},amount {amount}"

    valid = check_hash(hashed_text= signature, text= hash_text)
    print(valid)

    total = 0
    if valid == True:
        total += amount
    print(total)
```

## 3. Proof of work
![evidence_049.png](..%2F..%2Fassets%2Fevidence%2Fevidence_043-050%2Fevidence_049.png)
**Fig.3:** Evidence for quiz 049