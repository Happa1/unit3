from quiz_lib import DatabaseWorker

x = DatabaseWorker(name='bitcoin_exchange.db')

create_user = """CREATE TABLE if not exists users(
id INTEGER PRIMARY KEY,
name TEXT,
email TEXT)"""

x.run_query(create_user)

insert_query = """INSERT into users values (id, name, email) values
(560,'bob1','bob1@xyz'),(254,'bob2','bob2@xyz'),(920,'bob3','bob3@xyz'),(438,'bob4','bob4@xyz'),(744,'bob5','bob5@xyz'),(261,'bob6','bob6@xyz'),(371,'bob7','bob7@xyz'),(561,'bob8','bob8@xyz'),(488,'bob9','bob9@xyz')"""

x.run_query(insert_query)

search_query = """select * from (select * from ledger join user u on u.id = sender.id) t join user s s.id = t.receiver_id"""