# Quiz 048
![quiz_048.jpg](..%2F..%2Fassets%2Fprompt%2Fquiz_043-050%2Fquiz_048.jpg)
**Fig.1:** prompt of quiz 048

## 1. flow of chart
![quiz_diagram_048&049-2.jpg](..%2F..%2Fassets%2Fflowchart%2Fflowchart_043-050%2Fquiz_diagram_048%26049-2.jpg)
**Fig.2:** ER diagram of quiz 048

## 2. solution
```.py
from quiz_lib import DatabaseWorker, make_hash, check_hash

x = DatabaseWorker("bitcoin_exchange.db")

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

x.close()
```

## 3. Proof of work
![evidence_048.png](..%2F..%2Fassets%2Fevidence%2Fevidence_043-050%2Fevidence_048.png)
**Fig.3:** Evidence for quiz 048