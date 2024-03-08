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

    def search(self, query:str, multiple=False):
        results = self.cursor.execute(query)
        if multiple:
            return results.fetchall() # return multiple rows in a list
        return results.fetchone() # return single value

    def search_variable(self, query:str, *args, multiple=False):
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

    def create_candle(self, db):

        model=self.ids.model.text
        wax=self.ids.wax.text
        scent=self.ids.scent.text
        package=self.ids.package.text
        amount=self.ids.amount.text
        print(model,wax,scent,package,amount)

        if len(model) <1 or len(wax) <1 or len(scent) <1 or len(package) <1 or len(amount) <1:
            self.ids.order_error.text = "Please check the order again"
        else:
            model_id_query=f"""SELECT * from inventory where name=?"""
            model_id = db.search_variable(model_id_query,model,multiple=False)[0]
            wax_id_query=f"""SELECT * from inventory where name=?"""
            wax_id = db.search_variable(wax_id_query,wax,multiple=False)[0]
            scent_id_query=f"""SELECT * from inventory where name=?"""
            scent_id = db.search_variable(scent_id_query,scent,multiple=False)[0]

            order_list = [model_id, wax_id, scent_id, package, amount]
            print(order_list)
            price = 0
            for order in range(3):
                price_query = f"""SELECT selling_price from inventory where id=?"""
                each_price = db.search_variable(price_query, order_list[order], multiple=False)[0]
                price += each_price
            if order_list[3] == 'Yes':
                price += 30
            total_price = price * int(amount)

            query=f"""
            INSERT INTO orders 
            (model,wax,scent,package,amount,price,total_price)values(
            '{model_id}',
            '{wax_id}',
            '{scent_id}',
            '{package}',
            '{amount}',
            '{price}',
            '{total_price}'
            )"""
            db.run_query(query)