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

    hash_text = f"id{id},sender_id{sender_id},receiver_id{receiver_id},amount{amount}"

    valid = check_hash(hashed_text= signature, text= hash_text)
    print(valid)

x.close()
