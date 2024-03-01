from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from project_lib import DatabaseWorker, make_hash, check_hash
import sqlite3

db_name = "project_db"
db_connection = DatabaseWorker(name=db_name)


# db_connection.create()
# db_connection.close()
class HomeScreen(MDScreen):
    pass
#     def go_signup(self):
#         self.parent.current = "Signup"
#
#     def go_login(self):
#         self.parent.current = "Login"
#
#
class SignupScreen(MDScreen):
    pass
#     def try_signup(self):
#         uname = self.ids.uname.text
#         upass = self.ids.upass.text
#         upass_conf = self.ids.upass_conf.text
#
#         create = """CREATE TABLE if not exists users(
#                 id INTEGER PRIMARY KEY,
#                 username VARCHAR(30),
#                 password VARCHAR(30),
#                 hash TEXT);"""
#         db_connection.run_query(create)
#
#         if upass != upass_conf:
#             self.ids.error_label.text = "please check the password again."
#
#         else:
#             hash_text = f"name {uname},pass {upass}"
#             hash = make_hash(hash_text)
#             uname_upass_query = """
#                 SELECT * FROM users WHERE username = ? AND password = ?;
#             """
#
#             uname_upass = db_connection.search(uname_upass_query, uname, upass, multiple=True)
#
#             if uname_upass:
#                 self.ids.error_label.text = "Your password is invalid, so please enter again."
#
#             else:
#                 query = f"""
#                 INSERT into users (username, password, hash)
#                 values ('{uname}','{upass}','{hash}');
#                 """
#
#                 db_connection.run_query(query)
#
#                 self.parent.current = "Login"
#
#     def go_back_to_home(self):
#         self.parent.current = "Home"
#
#
class LoginScreen(MDScreen):
    pass
#     def try_login(self):
#         uname = self.ids.uname.text
#         upass = self.ids.upass.text
#
#         query = """
#         SELECT * from users where username=? and password=?"""
#
#         uname_upass = db_connection.search(query, uname, upass, multiple=True)
#
#         if uname_upass:
#             self.parent.current="Menu"
#         else:
#             self.ids.error_label.text = "Please enter the username and password again."
#
#     def go_back_to_home(self):
#         self.parent.current = "Home"


class MenuScreen(MDScreen):
    def screen_change(self,instance):
        key = instance.text
        menu_d ={"Take Order": "TakeOrder", "Check Descriptions": "Description", "Check Order": "CheckOrder", "Purchase materials": "Inventory", "Check ledger": "Ledger"}
        for k,v in menu_d.items():
            if key == k:
                screen = v
        self.parent.current = screen

    def go_back_to_home(self):
        self.parent.current = "Home"


class TakeOrderScreen(MDScreen):


    def go_back_to_menu(self):
        self.parent.current = "Menu"


class SuccessOrderScreen(MDScreen):
    def go_back_to_menu(self):
        self.parent.current = "Menu"


class ErrorOrderScreen(MDScreen):
    def go_back_to_menu(self):
        self.parent.current = "Menu"


class DescriptionScreen(MDScreen):
    def go_back_to_menu(self):
        self.parent.current = "Menu"


class CheckOrderScreen(MDScreen):
    def go_back_to_menu(self):
        self.parent.current = "Menu"


class InventoryScreen(MDScreen):
    def go_back_to_menu(self):
        self.parent.current = "Menu"


class LedgerScreen(MDScreen):
    def go_back_to_menu(self):
        self.parent.current = "Menu"


class project(MDApp):
    def build(self):
        Window.size = (700, 700)

    def changed(self):
        pass


test = project()
test.run()
