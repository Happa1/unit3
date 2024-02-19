from quiz_lib import DatabaseWorker, check_hash

x = DatabaseWorker(name='bitcoin_exchange.db')

sql_query = "SELECT SUM(amount) from ledger where (receiver_id = 920 or sender_id = 920)"
result = x.search(sql_query, True)[0][0]

print(result)