from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from quiz_lib import DatabaseWorker

class dropList(MDApp):
    def build (self):
        self.x=DatabaseWorker('bitcoin_exchange.db')
        query = "SELECT * from users"
        results = self.x.search(query, True)
        self.users = results
        Window.size=(500, 700)

    def open_menu(self, drop_item_element):
        # self.menu_item = [name for id, name in self.users]
        # self.menu_item = [c[1] for c in self.users]
        self.menu_item = []
        for c in self.users:
            name = c[1]
            self.menu_item.append(name)

        buttons_menu=[]
        for item in self.menu_item:
            btn_dict = {"text":item,
                        "viewclass":"OneLineListItem",
                        "on_release": lambda x=item: self.button_pressed(x)
                        }  #anonymous function def callback(x): return button_pressed(x)
            buttons_menu.append(btn_dict)

        self.menu = MDDropdownMenu(caller=drop_item_element, items=buttons_menu, width_mult=2)
        self.menu.open()

    def button_pressed(self,x):
        user = self.x.search(f"SELECT * from users where name='{x}'")
        if user:
            self.root.ids.customer.text = f"Customer {user[1]} with id{user[0]}"
            self.root.ids.dropdown_user.text = user[1]
        self.menu.dismiss()#closses the dropdowm menu

test = dropList()
test.run()
test.x.close()