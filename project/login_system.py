#login_system.py
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from my_lib import DatabaseWorker

class SignupScreen(MDScreen):
    def try_sringup(self):
        name=self.ids.uname.text
        email=self.ids.email.text
        upass=self.ids.upass.text
class LoginScreen(MDScreen):
    pass
class login(MDApp):
    def build(self):
        db_name = "project3_db"
        db = DatabaseWorker(name=db_name)
        db.create()
        db.close()

test = login()
test.run()

#
# name = 'alice'
# email = 'alice@xyz.com'
# password = 'pass456'
#
# query = f"""INSERT into users (email, password, username)
#         values ('{email}','{password}','{name}')"""
# # db.insert(query=query)
# db.insert(db.search('SELECT * from users', multiple=False))
# db.close()