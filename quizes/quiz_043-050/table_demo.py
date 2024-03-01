from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.screen import MDScreen
from quiz_lib import DatabaseWorker, make_hash


class TableScreen(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data_tables = None
        self.selected_rows = []
    def on_pre_enter(self, *args):
        #(name, size)
        columns_names = [('id', 40), ('Sender', 30), ('Receiver', 30), ('Amount', 40), ('Signature', 100)]
        self.data_tables = MDDataTable(
            size_hint = (.8, .5),
            pos_hint = {'center_x':.5, 'top':.8},
            use_pagination = False,
            check = True,
            column_data = columns_names
        )
        self.data_tables.bind(on_row_press=self.row_pressed)
        self.data_tables.bind(on_check_press=self.checkbox_pressed)
        self.add_widget(self.data_tables)
        self.update()

    def update(self):
        data = table.x.search(query='SELECT * from ledger', multiple=True)
        print(data)
        self.data_tables.update_row_data(
            None,data
        )

    def row_pressed(self, table, cell):
        print(f"Value clicked {cell.text}")

    def checkbox_pressed(self, table, current_row):
        print(f"Record checked {current_row}")
        #Here you could delete or update the record

    def save(self):
        sender = self.ids.sender.text
        receiver = self.ids.receiver.text
        amount = self.ids.amount.text
        print(sender, receiver, amount)
        signature = f'sender_id{sender},receiver_id{receiver},amount{amount}'
        save_query = f"""INSERT into ledger (sender_id, receiver_id, amount, signature)
        values ({sender}, {receiver}, {amount}, '{make_hash(signature)}')"""

        table.x.run_query(query=save_query)
        self.update()

class table(MDApp):
    x = DatabaseWorker('bitcoin_exchange.db') #class variable

    def build(self):
        pass

test = table()
test.run()
table.x.close()

