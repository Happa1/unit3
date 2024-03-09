import re
from datetime import datetime

from kivy.core.window import Window
from kivy.graphics import Color, Line, Rectangle
from kivy.metrics import dp
from kivy.properties import NumericProperty, ObjectProperty
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager
from kivy.utils import get_color_from_hex
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton, MDFlatButton, MDRectangleFlatButton, MDIconButton
from kivymd.uix.card import MDCard
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.dialog import MDDialog
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.navigationdrawer import MDNavigationDrawerMenu, MDNavigationLayout
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.font_definitions import theme_font_styles
from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path


from project_lib import DatabaseWorker, make_hash, check_hash

import sqlite3

db_name = "project_db"
db_connection = DatabaseWorker(name=db_name)

db_connection.create()
# db_connection.close()
class HomeScreen(MDScreen):
    create = """CREATE TABLE if not exists users(
                    id INTEGER PRIMARY KEY,
                    username VARCHAR(30),
                    hash TEXT);"""
    db_connection.run_query(create)

    pass
    def go_signup(self):
        self.parent.current = "Signup"

    def go_login(self):
        self.parent.current = "Login"

    query_inventory ="""CREATE TABLE if not exists inventory(
                 id INTEGER PRIMARY KEY,
                 name text,
                 genre text,
                 description text,
                 purchase_price int,
                 selling_price int,
                 amount int);"""

    query_orders="""CREATE TABLE if not exists orders(
                 id INTEGER PRIMARY KEY,
                 staff_id int,
                 model int,
                 wax int,
                 date TEXT,
                 scent int,
                 package TEXT,
                 amount INT,
                 price INT,
                 total_price INT
                 );
"""
    query_ledger="""CREATE TABLE if not exists ledger(
                 id INTEGER PRIMARY KEY,
                 staff_id INT,
                 date TEXT,
                 description TEXT,
                 price INT,
                 balance int);"""

    query_order_hisotry="""CREATE TABLE if not exists order_history(
                 id INTEGER PRIMARY KEY,
                 staff_id INT,
                 date TEXT,
                 model int,
                 wax int,
                 scent int,
                 package TEXT,
                 amount int);
"""

    query_purchases="""
    CREATE TABLE if not exists purchases(
                 id INTEGER PRIMARY KEY,
                 staff_id INT,
                 date TEXT,
                 material TEXT,
                 amount INT,
                 price INT,
                 total INT);"""

    db_connection.run_query(query_inventory)
    db_connection.run_query(query_orders)
    db_connection.run_query(query_purchases)
    db_connection.run_query(query_order_hisotry)
    db_connection.run_query(query_ledger)

class SignupScreen(MDScreen):
    dialog=None
    def try_signup(self):
        uname = self.ids.uname.text
        upass = self.ids.upass.text
        upass_conf = self.ids.upass_conf.text

        query_users = """CREATE TABLE if not exists users(
                id INTEGER PRIMARY KEY,
                username VARCHAR(30),
                hash TEXT);"""
        db_connection.run_query(query_users)

        if not 0<len(uname)<16 or not 0<len(upass)<9 or not 0<len(upass_conf)<9:
            if not self.dialog:
                self.dialog = MDDialog(
                    text="Please check the number of letters again.",
                    buttons=[MDFlatButton(
                        text="OK",
                        theme_text_color="Custom",
                        text_color=(1, 0.647, 0, 1),
                        on_release=self.cancel_pressed
                    )]
                )
            self.dialog.open()
        elif upass != upass_conf:
            if not self.dialog:
                self.dialog = MDDialog(
                    text="Please check the password again.",
                    buttons=[MDFlatButton(
                        text="OK",
                        theme_text_color="Custom",
                        text_color=(1, 0.647, 0, 1),
                        on_release=self.cancel_pressed
                    )]
                )
            self.dialog.open()

        else:
            hash_text = f"name {uname},pass {upass}"
            hash = make_hash(hash_text)
            results = db_connection.search(query="SELECT * FROM users", multiple=True)
            for row in results:
                signature = row[2]
                valid = check_hash(hashed_text=signature, text=hash_text)
                print(valid)

                if valid:
                    if not self.dialog:
                        self.dialog = MDDialog(
                            text="Your password is invalid, so please enter again.",
                            buttons=[MDFlatButton(
                                text="OK",
                                theme_text_color="Custom",
                                text_color=(1, 0.647, 0, 1),
                                on_release=self.cancel_pressed
                            )]
                        )
                    self.dialog.open()
                else:
                    query = f"""
                    INSERT into users (username, hash)
                    values ('{uname}','{hash}');
                    """
                    db_connection.run_query(query)
                    self.ids.uname.text=""
                    self.ids.upass.text=""
                    self.ids.upass_conf.text=""
                    self.parent.current = "Login"
    def cancel_pressed(self, *args):
        if self.dialog:
            self.dialog.dismiss()
        self.dialog=None

    def go_back_to_home(self):
        self.parent.current = "Home"

class LoginScreen(MDScreen): #Login
    dialog = None
    def try_login(self):
        uname = self.ids.uname.text
        upass = self.ids.upass.text
        query="SELECT * FROM users"
        results= db_connection.search(query=query,multiple=True)

        for row in results:
            signature = row[2]
            hash_text=f"name {uname},pass {upass}"
            valid=check_hash(hashed_text=signature, text=hash_text)

            if valid:
                app = MDApp.get_running_app()
                app.staff_id_value = row[0]
                self.ids.uname.text=""
                self.ids.upass.text=""
                self.parent.current = "Menu"
                app.root.ids.topbar.pos_hint = {"top": 1}
                print(valid)
                self.dialog=None
                break
            else:
                if not self.dialog:
                    self.dialog = MDDialog(
                        text="Your username or password is incorrect, so please enter again.",
                        buttons=[MDFlatButton(
                            text="OK",
                            theme_text_color="Custom",
                            text_color=(1, 0.647, 0, 1),
                            on_release=self.cancel_pressed
                        )]
                    )
                self.dialog.open()

    def cancel_pressed(self, *args):
        if self.dialog:
            self.dialog.dismiss()
        self.dialog=None

    def go_back_to_home(self):
        self.parent.current = "Home"

class MenuHeader(MDBoxLayout):
    '''An instance of the class that will be added to the menu header.'''

class NavigationMenu(MDNavigationDrawerMenu):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()

    def screen_change(self, instance):
        app = MDApp.get_running_app()
        print(f'staff_id: {app.staff_id_value}')
        key = instance.text
        menu_d = {"Take Order": "TakeOrder", "Description": "Description", "Check Order": "CheckOrder",
                  "Inventory": "Inventory", "Ledger": "Ledger", "Logout": "Home"}
        for k, v in menu_d.items():
            if key == k:
                screen = v
        self.parent.current = screen

class ContentNavigationDrawer(MDBoxLayout):
    pass

class MenuScreen(MDScreen):
    def screen_change(self,instance):
        app = MDApp.get_running_app()
        print(f'staff_id: {app.staff_id_value}')
        key = instance.text
        menu_d ={"Take Order": "TakeOrder", "Check Description": "Description", "Order History": "CheckOrder", "Check Inventory": "Inventory", "Check Ledger": "Ledger", "Logout":"Home"}
        for k,v in menu_d.items():
            if key == k:
                screen = v
        self.parent.current = screen

    def go_back_to_home(self):
        self.parent.current = "Home"

class TakeOrderScreen(MDScreen):
    dialog = None
    def build(self):
        pass
    def drop_menu(self, drop_item_element, drop_instance):
        key = drop_instance.text
        genre_d = {"Choose model":"model", "Choose wax":"wax", "Choose scent":"scent"}
        for k,v in genre_d.items():
            if key ==k:
                genre_value = v
        query = f"""
        SELECT * from inventory where genre=?
        """
        results = db_connection.search_variable(query, genre_value, multiple=True)

        self.model = results
        self.model_item=[]
        self.model_item = [c[1] for c in self.model]
        print(self.model_item)

        button_menu=[]
        for item in self.model_item:
            button_dict = {"text": str(item),
                        "viewclass": "OneLineListItem",
                        "on_release": lambda x=item: self.button_pressed(x)}
            button_menu.append(button_dict)

        self.menu = MDDropdownMenu(caller=drop_item_element,
                                   ver_growth="down",
                                   items=button_menu,
                                   width_mult=4,
                                   position="center"
                                   )
        self.menu.open()

    def drop_amount(self, drop_item_element, drop_instance):
        button_menu=[]
        for i in range(1,6):
            button_dict = {"text": str(i),
                        "viewclass": "OneLineListItem",
                        "on_release": lambda x=i: self.button_pressed_amount(x)}
            button_menu.append(button_dict)

        self.menu = MDDropdownMenu(caller=drop_item_element,
                                   ver_growth="down",
                                   items=button_menu,
                                   width_mult=4,
                                   position="center"
                                   )
        self.menu.open()

    def drop_package(self, drop_item_element, drop_instance):
        button_option = ["Yes", "No"]
        button_menu=[]
        for i in button_option:
            button_dict = {"text": str(i),
                           "viewclass": "OneLineListItem",
                           "on_release": lambda x=i: self.button_pressed_package(x)}
            button_menu.append(button_dict)

        self.menu = MDDropdownMenu(caller=drop_item_element,
                                   ver_growth="down",
                                   items=button_menu,
                                   width_mult=4,
                                   position="center"
                                   )
        self.menu.open()

    def button_pressed(self,x):
        item = db_connection.search(f"SELECT * from inventory where name='{x}'")
        print(f'item{item}')
        price=item[5]
        label = self.ids[item[2]] #item[2] =genre
        if label:
            label.text = item[1]
            self.ids.candle_image.source=f"Project_Images/{item[8]}"

        self.menu.dismiss()

    def button_pressed_amount(self,x):
        self.ids.amount.text = str(x)
        self.menu.dismiss()

    def button_pressed_package(self, x):
        self.ids.package.text = x
        self.menu.dismiss()

    def make_more_candle(self):
        app = MDApp.get_running_app()
        print(f'staff_id: {app.staff_id_value}')
        model=self.ids.model.text
        wax=self.ids.wax.text
        scent=self.ids.scent.text
        package=self.ids.package.text
        amount=self.ids.amount.text
        print(model,wax,scent,package,amount)

        if len(model) <1 or len(wax) <1 or len(scent) <1 or len(package) <1 or len(amount) <1:
            if not self.dialog:
                self.dialog = MDDialog(
                    text="Please check the order again.",
                    buttons=[
                        MDFlatButton(
                            text="CLOSE",
                            theme_text_color="Custom",
                            text_color=(1, 0.647, 0, 1),
                            on_release=self.cancel_pressed)
                    ],
                )
            self.dialog.open()

        else:
            model_id_query=f"""SELECT * from inventory where name=?"""
            model_id = db_connection.search_variable(model_id_query,model,multiple=False)[0]
            wax_id_query=f"""SELECT * from inventory where name=?"""
            wax_id = db_connection.search_variable(wax_id_query,wax,multiple=False)[0]
            scent_id_query=f"""SELECT * from inventory where name=?"""
            scent_id = db_connection.search_variable(scent_id_query,scent,multiple=False)[0]

            order_list = [model_id, wax_id, scent_id, package, amount]
            print(order_list)
            price = 0
            for order in range(3):
                price_query = f"""SELECT selling_price from inventory where id=?"""
                each_price = db_connection.search_variable(price_query, order_list[order], multiple=False)[0]
                price += each_price
            if order_list[3] == 'Yes':
                price += 30
            total_price = price * int(amount)

            query=f"""
            INSERT INTO orders 
            (model,wax,scent,package,amount,price,total_price,staff_id,date)values(
            '{model_id}',
            '{wax_id}',
            '{scent_id}',
            '{package}',
            '{amount}',
            '{price}',
            '{total_price}',
            '{app.staff_id_value}',
            '{app.today_date}'
            )"""

            db_connection.run_query(query) #insert order in table orders
            self.parent.current = "TakeOrder"
            self.ids.model.text=""
            self.ids.wax.text =""
            self.ids.scent.text=""
            self.ids.package.text=""
            self.ids.amount.text=""

    def cancel_pressed(self, *args):
        if self.dialog:
            self.dialog.dismiss()
    def go_to_check(self):
        app = MDApp.get_running_app()
        count_query="""
        SELECT COUNT(*) FROM orders"""
        count_result=db_connection.search(count_query)[0]

        model = self.ids.model.text
        wax = self.ids.wax.text
        scent = self.ids.scent.text
        package = self.ids.package.text
        amount = self.ids.amount.text
        print(model, wax, scent, package, amount)

        if len(model) > 1 or len(wax) > 1 or len(scent) > 1 or len(package) > 1 or len(amount) > 1:#even if one section is filled
            if len(model) < 1 or len(wax) < 1 or len(scent) < 1 or len(package) < 1 or len(amount) < 1:
                if not self.dialog:
                    self.dialog = MDDialog(
                        text="Please check the order again.",
                        buttons=[
                            MDFlatButton(
                                text="CLOSE",
                                theme_text_color="Custom",
                                text_color=(1, 0.647, 0, 1),
                                on_release=self.cancel_pressed)
                        ],
                    )
                self.dialog.open()
            else:
                model_id_query = f"""SELECT * from inventory where name=?"""
                model_id = db_connection.search_variable(model_id_query, model, multiple=False)[0]
                wax_id_query = f"""SELECT * from inventory where name=?"""
                wax_id = db_connection.search_variable(wax_id_query, wax, multiple=False)[0]
                scent_id_query = f"""SELECT * from inventory where name=?"""
                scent_id = db_connection.search_variable(scent_id_query, scent, multiple=False)[0]

                order_list = [model_id, wax_id, scent_id, package, amount]
                print(order_list)
                price = 0
                for order in range(3):
                    price_query = f"""SELECT selling_price from inventory where id=?"""
                    each_price = db_connection.search_variable(price_query, order_list[order], multiple=False)[0]
                    price += each_price
                if order_list[3] == 'Yes':
                    price += 30
                total_price = price * int(amount)

                query = f"""
                        INSERT INTO orders 
                        (model,wax,scent,package,amount,price,total_price,staff_id,date)values(
                        '{model_id}',
                        '{wax_id}',
                        '{scent_id}',
                        '{package}',
                        '{amount}',
                        '{price}',
                        '{total_price}',
                        '{app.staff_id_value}',
                        '{app.today_date}'
                        )"""
                db_connection.run_query(query)
                self.ids.model.text = ""
                self.ids.wax.text = ""
                self.ids.scent.text = ""
                self.ids.package.text = ""
                self.ids.amount.text = ""
                self.parent.current="Check"
        elif count_result>1: #if there is no data in the text, but in the orders
            self.parent.current = "Check"
        elif count_result<1: #if there is no data in the orders
            if not self.dialog:
                self.dialog = MDDialog(
                    text="Please make the order.",
                    buttons=[
                        MDFlatButton(
                            text="CLOSE",
                            theme_text_color="Custom",
                            text_color=(1, 0.647, 0, 1),
                            on_release=self.cancel_pressed)
                    ],
                )
            self.dialog.open()

    def go_back_to_menu(self):
        self.parent.current = "Menu"

class CheckScreen(MDScreen):
    dialog=None
    def __init__(self, **kwargs):
        super(CheckScreen, self).__init__(**kwargs)

    def on_pre_enter(self, *args):
        columns_names = [('No.',40),('Model',70),('Wax', 40), ('Scent', 40),('Package', 40),('Price',40), ('Amount',30),('Total',50)]
        self.data_tables = MDDataTable(
            size_hint=(.9, .6),
            pos_hint={'center_x': .5, 'top': .8},
            use_pagination=True,
            check=True,
            background_color_header="#FFC697",
            background_color_selected_cell="f5deb3",
            rows_num=10,
            column_data=columns_names,
        )
        # self.data_tables.bind(on_row_press=self.on_row_press)
        self.data_tables.bind(on_check_press=self.checkbox_pressed)
        self.add_widget(self.data_tables)
        self.update()
    def update(self):
        data = db_connection.search(query='SELECT id, model, wax, scent, package, price, amount, total_price FROM orders', multiple=True)
        candle=db_connection.search(query=f"SELECT description from inventory, orders where inventory.id=orders.model")[0]
        wax_name=db_connection.search(query=f"SELECT name from inventory, orders where inventory.id=orders.wax")[0]
        scent_name=db_connection.search(query=f"SELECT name from inventory, orders where inventory.id=orders.scent")[0]
        calculated_data = [(id,candle, wax_name, scent_name, package, price, amount, total_price) for
                           id,model, wax, scent, package, price, amount, total_price in data]
        self.data_tables.update_row_data(
            None, calculated_data
        )
        total_price_query=db_connection.search(query="SELECT SUM(total_price) FROM orders")[0]
        self.ids.total_price_label.text=f'¥ {total_price_query}'
    def checkbox_pressed(self, table, current_row):
        self.ids.select_item.text=f"Select: {str(current_row[0])}"
        self.check_select=current_row
        print(current_row[0])

    def item_delete(self):
        m = re.findall(r'\d+', self.ids.select_item.text)
        print(m[0])
        item_id=int(m[0])
        db_connection.run_query(query=f"""delete FROM orders WHERE id={item_id}""")
        self.update()

    def lets_check(self):
        if not self.dialog:
            self.dialog = MDDialog(
                text="I would like to proceed with the payment. Is it okay?",
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        theme_text_color="Custom",
                        text_color=(1, 0.647, 0, 1),
                        on_release=self.cancel_pressed
                    ),
                    MDFlatButton(
                        text="PROCEED",
                        theme_text_color="Custom",
                        text_color=(1, 0.647, 0, 1),
                        on_release=self.proceed_pressed
                    ),
                ],
            )
        self.dialog.open()

    def cancel_pressed(self,*args):
        if self.dialog:
            self.dialog.dismiss()

    def proceed_pressed(self,*args):
        app = MDApp.get_running_app()

        count_query="""
        SELECT COUNT(*) FROM orders"""
        count_result=db_connection.search(count_query)[0]
        print(count_result)


        if self.dialog:
            order_history_query = """
                INSERT INTO order_history (staff_id, date, model, wax, scent, package, amount)
                SELECT staff_id, date, model, wax, scent, package, amount
                FROM orders;
            """
            ledger_query = """
                INSERT INTO ledger (order_id, staff_id, date, price,description)
                SELECT id, staff_id, date, price,'sale'
                FROM orders;
            """

            for i in range(count_result):
                update_model_inventory = f"""
                    UPDATE inventory
                    SET amount = (SELECT amount FROM inventory WHERE inventory.id
                         = (SELECT model FROM orders WHERE orders.id = {i+1})) 
                         - (SELECT amount FROM orders WHERE orders.id = {i+1})
                    WHERE inventory.id = (SELECT model FROM orders WHERE orders.id = {i+1}
                    );
                """
                db_connection.run_query(update_model_inventory)

                update_wax_inventory = f"""
                                    UPDATE inventory
                                    SET amount = (SELECT amount FROM inventory WHERE inventory.id
                                         = (SELECT wax FROM orders WHERE orders.id = {i + 1})) 
                                         - (SELECT amount FROM orders WHERE orders.id = {i + 1})
                                    WHERE inventory.id = (SELECT wax FROM orders WHERE orders.id = {i + 1}
                                    );
                                """
                db_connection.run_query(update_wax_inventory)

                update_scent_inventory = f"""
                                    UPDATE inventory
                                    SET amount = (SELECT amount FROM inventory WHERE inventory.id
                                         = (SELECT scent FROM orders WHERE orders.id = {i + 1})) 
                                         - (SELECT amount FROM orders WHERE orders.id = {i + 1})
                                    WHERE inventory.id = (SELECT scent FROM orders WHERE orders.id = {i + 1}
                                    );
                                """
                db_connection.run_query(update_scent_inventory)

                update_package_inventory = f"""
                                    UPDATE inventory
                                    SET amount = (SELECT amount FROM inventory WHERE inventory.id= 16)
                                         - (SELECT amount FROM orders WHERE orders.id = {i + 1} and orders.package = 'Yes')
                                    WHERE inventory.id = 16
                                    ;
                                """
                db_connection.run_query(update_package_inventory)

            db_connection.run_query(order_history_query)
            db_connection.run_query(ledger_query)

            db_connection.run_query(query="""DELETE FROM orders""")
            self.dialog.dismiss()
            self.parent.current = "Success"

    def go_back_to_menu(self):
        self.parent.current = "TakeOrder"

class SuccessOrderScreen(MDScreen):
    def go_back_to_menu(self):
        self.parent.current = "Menu"

class ErrorOrderScreen(MDScreen):
    def go_back_to_menu(self):
        self.parent.current = "Menu"

class MD3Card(MDCard):
    '''Implements a material design v3 card.'''

class DescriptionScreen(MDScreen):
    dialog=None
    def __init__(self, **kwargs):
        super(DescriptionScreen, self).__init__(**kwargs)
    def on_enter(self, *args):
        count_query = """
                        SELECT COUNT(*) FROM inventory"""
        count_result = db_connection.search(count_query)[0]
        box_count = count_result  # 追加する MDBoxLayout の数を指定
        self.update_layout(box_count)
        print(f'box_cont: {box_count}')

    def update_layout(self, box_count, box_layout=None):
        container = self.ids.container_desc
        container.clear_widgets()  # delete all children widget
        source='Project_Images/'

        for i in range(box_count):
            count = i+1
            image_query = f"""SELECT image, name, id from inventory where id={count}"""
            material_name = db_connection.search_variable(image_query, multiple=False)[1]
            image_name = db_connection.search_variable(image_query, multiple=False)[0]
            id_numb = db_connection.search_variable(image_query, multiple=False)[2]
            print(f'{material_name}, {source+image_name}',{id_numb})
            box_layout = MDBoxLayout(orientation='vertical', adaptive_size=True, spacing="4dp")

            box_layout.add_widget(
                MD3Card(
                    MDRelativeLayout(
                        MDIconButton(
                            text=f"{id_numb}",
                            icon="dots-vertical",
                            pos_hint={"top": 1, "right": 1},
                            md_bg_color= "FFC697",
                            on_press= lambda x=id_numb: self.press_material(x)
                        ),
                        MDLabel(
                            text=material_name.capitalize(),
                            adaptive_size=True,
                            color="grey",
                            pos_hint={"bottom": 1, "left": 1},
                            size_hint_x=1,
                            halign="center"
                        ),
                        Image(
                            source=f'{source+image_name}',
                            size_hint_y= None,
                            height= '100dp', # Set the desired height
                            width= '200dp',  # Set the desired width
                            pos_hint = {"center_x": .5, "center_y": .5}
            )
                    ),
                    line_color=(0.2, 0.2, 0.2, 0.8),
                    orientation="vertical",
                    padding="4dp",
                    size_hint=(None, None),
                    size=("300dp", "150dp"),
                    md_bg_color="ffdead",
                    shadow_softness=0,
                    shadow_offset=(0, 0),
                )
            )

            container.add_widget(box_layout)  # 新しい MDBoxLayout を追加

    def press_material(self, numb):
        print(f'number {numb.text}')
        number=int(numb.text)
        print(f'self numb {number}')
        print(type(number))
        text_query=f"""SELECT description from inventory where id={number}"""
        print(text_query)
        text_desc = db_connection.search(text_query,multiple=False)[0]

        print(text_desc)
        if not self.dialog:
            self.dialog = MDDialog(
                text=f"{text_desc}",
                buttons=[
                    MDFlatButton(
                        text="CLOSE",
                        theme_text_color="Custom",
                        text_color=(1, 0.647, 0, 1),
                        on_release=self.cancel_pressed)
                ],
            )
        else:
            self.dialog.text=f"{text_desc}"
        self.dialog.open()

    def cancel_pressed(self, *args):
        if self.dialog:
            self.dialog.dismiss()

    def go_back_to_menu(self):
        self.parent.current = "Menu"

class CheckOrderScreen(MDScreen):
    dialog=None
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data_tables = None
        self.selected_rows = []

    def on_pre_enter(self, *args):
        columns_names = [('Staff',50),('Prodct', 100), ('Wax', 100),('Scent',100)]
        # columns_names = [column for column in columns_names if column[0] not in ['id', 'genre']]

        self.data_tables = MDDataTable(
            size_hint=(.9, .6),
            pos_hint={'center_x': .5, 'top': .7},
            use_pagination=True,
            check=True,
            background_color_header="#FFC697",
            background_color_selected_cell="f5deb3",
            rows_num=10,
            column_data=columns_names
        )
        self.data_tables.bind(on_row_press=self.row_pressed)
        self.data_tables.bind(on_check_press=self.checkbox_pressed)
        self.add_widget(self.data_tables)
        self.update()

    def update(self):
        data = db_connection.search(query="""SELECT users.username AS staff, inventory.name AS candle, inventory.name AS wax, inventory.name AS scent
                                                FROM users
                                                JOIN order_history ON order_history.staff_id = users.id
                                                JOIN inventory ON order_history.model = inventory.id OR order_history.wax = inventory.id OR order_history.scent = inventory.id;
""", multiple=True)
        # Perform calculations and update the data before updating the MDDataTable
        calculated_data = [(staff, candle, wax, scent) for
                           staff, candle, wax, scent in data]
        print(data)
        print(calculated_data)
        self.data_tables.update_row_data(
            None, calculated_data
        )

    def row_pressed(self, table, cell):
        print(f"Value clicked {cell.text}")

    def checkbox_pressed(self, table, current_row):
        print(f"Record checked {current_row[1]}")
        self.ids.checked_item.text=str(current_row[1])
        # Here you could delete or update the record

    def go_back_to_menu(self):
        self.parent.current = "Menu"

class InventoryScreen(MDScreen):
    dialog=None
    calculate=True
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data_tables = None
        self.selected_rows = []

    def on_pre_enter(self, *args):
        columns_names = [('number',50),('material', 100), ('amount', 100),('shortage',100)]
        # columns_names = [column for column in columns_names if column[0] not in ['id', 'genre']]

        self.data_tables = MDDataTable(
            size_hint=(.9, .6),
            pos_hint={'center_x': .5, 'top': .8},
            use_pagination=True,
            check=True,
            background_color_header="#FFC697",
            background_color_selected_cell="f5deb3",
            rows_num=10,
            column_data=columns_names,
        )
        self.data_tables.bind(on_row_press=self.row_pressed)
        self.data_tables.bind(on_check_press=self.checkbox_pressed)
        self.add_widget(self.data_tables)
        self.update()


    def update(self):
        data = db_connection.search(query='SELECT id, name, amount, default_amount FROM inventory', multiple=True)
        # Perform calculations and update the data before updating the MDDataTable
        calculated_data = [(id, name, amount, (default_amount - amount)) for
                           id, name, amount, default_amount in data]
        # print(data)
        print(calculated_data)
        self.data_tables.update_row_data(
            None, calculated_data
        )

    def calculate_pressed(self):
        if self.calculate:
            data = db_connection.search(query='SELECT id, name, amount, default_amount FROM inventory', multiple=True)
            calculated_data = [(id, name, amount, (default_amount - amount)) for
                               id, name, amount, default_amount in data]
            calculated_data_2=[]
            for row in calculated_data:
                if row[3] >=5:
                    calculated_data_2.append(row)

            self.data_tables.update_row_data(
                None, calculated_data_2
            )
            self.calculate=None
            self.ids.calculate_btn.text="Original"
            self.ids.calculate_btn.icon = "backup-restore"

        else:
            data = db_connection.search(query='SELECT id, name, amount, default_amount FROM inventory', multiple=True)
            # Perform calculations and update the data before updating the MDDataTable
            calculated_data = [(id, name, amount, (default_amount - amount)) for
                               id, name, amount, default_amount in data]
            # print(data)
            print(calculated_data)
            self.data_tables.update_row_data(
                None, calculated_data
            )
            self.calculate = True
            self.ids.calculate_btn.text = "Calculate"
            self.ids.calculate_btn.icon = "calculator"

    def row_pressed(self, table, cell):
        print(f"Value clicked {cell.text}")

    def checkbox_pressed(self, table, current_row):
        self.ids.checked_item.text=str(current_row[1])
        # Here you could delete or update the record

    def add_cart(self):
        app = MDApp.get_running_app()
        amount=self.ids.amount_of_inv.text
        print('a')

        if len(amount)<1 or not amount.isdigit():
            if not self.dialog:
                self.dialog = MDDialog(
                    text="Please enter the amount in integer",
                    buttons=[MDFlatButton(
                        text="OK",
                        theme_text_color="Custom",
                        text_color=(1, 0.647, 0, 1),
                        on_release=self.cancel_pressed
                    )]
                )
            self.dialog.open()

        else:
            item=self.ids.checked_item.text
            search_query=f"""SELECT id, purchase_price FROM inventory WHERE name='{item}'"""
            result=db_connection.search(search_query,multiple=False)
            print(result)
            total=int(result[1]) * int(amount)

            query = f"""
            INSERT INTO purchases
            (staff_id, date, material, amount, price, total)
            values (
            '{app.staff_id_value}',
            '{app.today_date}',
            {result[0]},
            {amount},
            {result[1]},
            {total}
            )"""
            db_connection.run_query(query)
            self.ids.checked_item.text="Please check the item."
            self.ids.amount_of_inv.text=""

    def cancel_pressed(self, *args):
        if self.dialog:
            self.dialog.dismiss()
    def go_purchase(self):
        count_query = """
                        SELECT COUNT(*) FROM purchases"""
        count_result = db_connection.search(count_query)[0]
        if count_result<1:
            if not self.dialog:
                self.dialog = MDDialog(
                    text="Please add items in the cart",
                    buttons=[MDFlatButton(
                        text="OK",
                        theme_text_color="Custom",
                        text_color=(1, 0.647, 0, 1),
                        on_release=self.cancel_pressed
                    )]
                )
            self.dialog.open()
        else:
            self.parent.current="InventoryOrder"

    def go_back_to_menu(self):
        self.parent.current = "Menu"

class InventoryOrderScreen(MDScreen):
    dialog=None
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data_tables = None
        self.selected_rows = []
    def on_pre_enter(self, *args):
        columns_names = [('No.',100),('Name',100),('Price', 50), ('Amount', 50),('Total',100)]
        self.data_tables = MDDataTable(
            size_hint=(.9, .6),
            pos_hint={'center_x': .5, 'top': .8},
            use_pagination=True,
            check=True,
            background_color_header="#FFC697",
            background_color_selected_cell="f5deb3",
            rows_num=10,
            column_data=columns_names,
        )
        self.data_tables.bind(on_row_press=self.on_row_press)
        self.data_tables.bind(on_check_press=self.inv_checkbox_pressed)
        self.add_widget(self.data_tables)
        self.update()
    def update(self):
        data = db_connection.search(query='SELECT id, material, price, amount, total FROM purchases', multiple=True)
        material=db_connection.search(query='SELECT inventory.name FROM inventory,purchases where inventory.id = purchases.material', multiple=False)[0]
        calculated_data = [(id, material, amount, price, total) for
                           id,name, amount, price, total in data]
        self.data_tables.update_row_data(
            None, calculated_data
        )
        total_price_query = db_connection.search(query="SELECT SUM(total) FROM purchases")[0]
        self.ids.total_price_label.text = f'¥ {total_price_query}'


    def on_row_press(self, table, instance_row):
        if hasattr(instance_row, '__iter__'):
            # Now you can unpack these values if needed
            material, amount, price, total = instance_row
            print(f"Row pressed - Material: {material}, Amount: {amount}, Price: {price}, Total: {total}")
        else:
            print(f"Row pressed - Unable to unpack values from non-iterable object")

    def inv_checkbox_pressed(self, table, current_row):
        self.ids.select_item.text = f"Select: {str(current_row[0])}"

    def item_delete(self):
        m = re.findall(r'\d+', self.ids.select_item.text)
        print(m[0])
        item_id=int(m[0])
        db_connection.run_query(query=f"""delete FROM purchases WHERE id={item_id}""")
        self.update()

    def make_purchase(self):
        if not self.dialog:
            self.dialog = MDDialog(
                text="I would like to proceed with the payment. Is it okay?",
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        theme_text_color="Custom",
                        text_color=(1, 0.647, 0, 1),
                        on_release=self.cancel_pressed
                    ),
                    MDFlatButton(
                        text="PROCEED",
                        theme_text_color="Custom",
                        text_color=(1, 0.647, 0, 1),
                        on_release=self.proceed_pressed
                    ),
                ],
            )
        self.dialog.open()

    def cancel_pressed(self, *args):
        if self.dialog:
            self.dialog.dismiss()

    def proceed_pressed(self, *args):
        app = MDApp.get_running_app()

        count_query = """
                SELECT COUNT(*) FROM purchases"""
        count_result = db_connection.search(count_query)[0]
        print(count_result)

        if self.dialog:
            ledger_query = f"""
                INSERT INTO ledger (order_id, staff_id, date, price,description)
                SELECT id, staff_id, date, -1 * total AS price,'purchase'
                FROM purchases;
                
            """

            for i in range(count_result):
                update_purchased_inventory = f"""
                    UPDATE inventory
                    SET amount = (SELECT amount FROM inventory WHERE inventory.id
                         = (SELECT material FROM purchases WHERE purchases.id = {i+1})) 
                         + (SELECT amount FROM purchases WHERE purchases.id = {i+1})
                    WHERE inventory.id = (SELECT purchases.material FROM purchases WHERE purchases.id = {i+1}
                    );
                """
                db_connection.run_query(update_purchased_inventory)
            db_connection.run_query(ledger_query)

        db_connection.run_query(query="""DELETE FROM purchases""")

        self.dialog.dismiss()
        self.parent.current = "Inventory"

    def go_back_to_menu(self):
        self.parent.current = "Inventory"

class LedgerScreen(MDScreen):
    dialog = None
    ascending = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data_tables = None
        self.selected_rows = []

    def on_pre_enter(self, *args):
        columns_names = [('Date',80),('Staff', 80), ('Description', 80),('Price', 80),('Balance',100)]
        # columns_names = [column for column in columns_names if column[0] not in ['id', 'genre']]
        self.data_tables = MDDataTable(
            size_hint=(.9, .6),
            pos_hint={'center_x': .5, 'top': .65},
            use_pagination=True,
            check=True,
            background_color_header="#FFC697",
            background_color_selected_cell="f5deb3",
            rows_num=10,
            column_data=columns_names
        )
        self.data_tables.bind(on_row_press=self.row_pressed)
        self.add_widget(self.data_tables)
        self.update()

    def update(self):
        data = db_connection.search(query='SELECT date, staff_id, description, price, balance FROM ledger', multiple=True)
        staff_name = db_connection.search(
            query='SELECT users.username FROM users, ledger where ledger.staff_id = users.id',
            multiple=False)[0]
        # Perform calculations and update the data before updating the MDDataTable
        calculated_data = [(date, staff_name, description, price, balance) for
                           date, staff_id, description, price, balance in data]
        print(data)
        print(calculated_data)
        self.data_tables.update_row_data(
            None, calculated_data
        )

    def row_pressed(self, table, cell):
        print(f"Value clicked {cell.text}")

    def date_descending_pressed(self):
        if self.ascending:
            descending_query="""
            SELECT date, staff_id, description, price, balance FROM ledger
            ORDER BY id DESC;  -- 降順
            """
            descending_data = db_connection.search(query=descending_query, multiple=True)
            staff_name = db_connection.search(
                query='SELECT users.username FROM users, ledger where ledger.staff_id = users.id',
                multiple=False)[0]
            # Perform calculations and update the data before updating the MDDataTable
            calculated_data = [(date, staff_name, description, price, balance) for
                               date, staff_id, description, price, balance in descending_data]
            # updateメソッドを呼び出す
            self.data_tables.update_row_data(
                None, calculated_data
            )
            self.ascending=None
            self.ids.date_descending.text="Date Ascending"
            self.ids.date_descending.icon = "sort-calendar-ascending"

        else:
            ascending_query = """
                        SELECT date, staff_id, description, price, balance FROM ledger
                        ORDER BY id ASC;  -- 降順
                        """
            descending_data = db_connection.search(query=ascending_query, multiple=True)
            staff_name = db_connection.search(
                query='SELECT users.username FROM users, ledger where ledger.staff_id = users.id',
                multiple=False)[0]
            # Perform calculations and update the data before updating the MDDataTable
            calculated_data = [(date, staff_name, description, price, balance) for
                               date, staff_id, description, price, balance in descending_data]
            # updateメソッドを呼び出す
            self.data_tables.update_row_data(
                None, calculated_data
            )
            self.ascending = True
            self.ids.date_descending.text = "Date Descending"
            self.ids.date_descending.icon = "sort-calendar-descending"



    def go_back_to_menu(self):
        self.parent.current = "Menu"

class project(MDApp):
    # app = MDApp.get_running_app()
#     app.staff_id_value = uname_upass[0][0]
    staff_id_value=0#あとでnoneかなんかに変える
    today_date = datetime.now().date()
    print(today_date)

    def build(self):
        # self.theme_cls.primary_palette = "Orange"
        Window.size = (1000, 800)
        self.theme_cls.theme_style = "Light"

    def drop_menu(self):
        pass

    def changed(self):
        pass


test = project()
test.run()
