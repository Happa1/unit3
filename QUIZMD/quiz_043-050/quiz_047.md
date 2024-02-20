# Quiz 047
![quiz_047.jpg](..%2F..%2Fassets%2Fprompt%2Fquiz_043-050%2Fquiz_047.jpg)
**Fig.1:** prompt of quiz 047

## 1. flow of chart
![quiz_diagram_047.jpg](..%2F..%2Fassets%2Fflowchart%2Fflowchart_043-050%2Fquiz_diagram_047.jpg)
**Fig.2:** ER diagram of quiz 047

## 2. solution
```.py
import sqlite3

from kivymd.app import MDApp
from quiz_lib import DatabaseWorker, make_hash, check_hash

class quiz_046(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.components = {"basic":0, "helthe":0, "income_tax":0, "inhabitant":0, "total":0, "pension":0, "hash":""}
        self.db_connection = DatabaseWorker("payments.db")

    def build(self):
        return

    def save(self):
        pass

    def update(self):
        #This function updates all the labels in the form using the base salary and the percentage
        # Pseudocode
        # 1- get the base salary from the GUI
        # 2- if base salary define total=int(base) and an empty string to store build a hash (for_hash="") if no base then end the function
        # 3- for Each TextField with ids: "inhabitant","income_tax","pension","health" get the text property
        # 4- if the TextField.text has a number (value), calculate the equation new_value="(base*int(value)//100) JPY" and subbctract the equation to the total
        # 5- if no: then new_value = " JPY"
        # 6- set the label next to the TextField (inhabitant_label, income_tax_label, etc) to the variable new_value
        # 7- concatenate to the hash variable the f"{id}{value}"
        # 8- set the text of the element id=total to the total with the JPY symbol
        # 9- encrypt the hash and change the text of the label with id=hash to the last 50 characters of the hash

        #calculate total
        ids = ["inhabitant", "income_tax", "pension", "health"]
        base = self.root.ids.base.text
        if base:
            base_int = int(base)
            hash = ""
            pension = int(self.root.ids.pension.text or'0')
            health = int(self.root.ids.health.text or'0')
            income_tax = int(self.root.ids.income_tax.text or'0')
            inhabitant = int(self.root.ids.inhabitant.text or'0')

            pension_jpy = base_int * pension //100
            health_jpy = base_int * health //100
            income_tax_jpy = base_int * income_tax //100
            inhabitant_jpy = base_int * inhabitant //100

            self.root.ids.pension_label.text = f"{pension_jpy} JPY"
            self.root.ids.health_label.text = f"{health_jpy} JPY"
            self.root.ids.income_tax_label.text = f"{income_tax_jpy} JPY"
            self.root.ids.inhabitant_label.text = f"{inhabitant_jpy} JPY"
            total = base_int - pension_jpy - health_jpy - income_tax_jpy -inhabitant_jpy
            self.root.ids.salary_label.text = f"{total} JPY"

            hash = f"base{base_int},inhabitant{inhabitant_jpy},income{income_tax_jpy},pension{pension_jpy},health{health_jpy},total{total}"

            self.components['hash'] = hash
            self.components['total'] = total
            self.components['base'] = base_int
            self.components['pension'] = pension_jpy
            self.components['health'] = health_jpy
            self.components['income_tax'] = income_tax_jpy
            self.components['inhabitant'] = inhabitant_jpy

            # update the percentage

    def save(self):
        hash = make_hash(self.components['hash'])
        total = self.components['total']
        base_int = self.components['base']
        pension_jpy = self.components['pension']
        health_jpy = self.components['health']
        income_tax_jpy = self.components['income_tax']
        inhabitant_jpy = self.components['inhabitant']
        #inhabitant4,income_tax3,pension2,health1,total1103  (here the numbers next to the category are percentages)

        query = f"""INSERT into payments(base, inhabitant, income_tax, pension, health, total, hash)
        values ({base_int},{inhabitant_jpy},{income_tax_jpy},{pension_jpy},{health_jpy},{total},'{hash}')
        """
        self.db_connection.run_query(query)
        # db = database_worker("payments.db")
        # db.run_save(query)
        # db.close()
        self.root.ids.hash.text = f"Payment saved"

    def clear(self):
        for label in ["base", "inhabitant","income_tax","pension","health"]:
            self.root.ids[label].text = ""
            self.root.ids[label+"_label"].text = " JPY"

        self.root.ids["salary_label"].text = " JPY"
        self.root.ids.hash.text = "----"


test = quiz_046()
create = """CREATE TABLE if not exists payments(
        id INTEGER PRIMARY KEY,
        base INT,
        health INT,
        pension INT,
        income_tax INT,
        inhabitant INT,
        hash TEXT,
        total INT
    )"""

my_db = DatabaseWorker("payments.db")
my_db.run_query(query=create)

sql_query = "SELECT * from payments"

results = my_db.search(query=sql_query, multiple=True)

for row in results:
    base_int = row[1]
    health_jpy = row[2]
    pension_jpy = row[3]
    income_tax_jpy = row[4]
    inhabitant_jpy = row[5]
    signature = row[6]
    total = row[7]
    hash_text = f"base{base_int},inhabitant{inhabitant_jpy},income{income_tax_jpy},pension{pension_jpy},health{health_jpy},total{total}"
    valid = check_hash(hashed_text= signature, text= hash_text)
    print(valid)

my_db.close()
test.run()
test.db_connection.close()

```

```.kv
MDScreen:
    id:bck
    size: 200, 500

    MDBoxLayout:
        id: bck
        size_hint: .8,.9
        md_bg_color: "#F2F2F2"
        orientation: "vertical"
        pos_hint: {"center_x":.5, "center_y":.5}
        spacing: dp(10)

        MDLabel:
            text:"Compensation Calculator"
            halign: "center"
            font_style:"H4"
            color: "#222222"

        MDBoxLayout:
            size_hint_x: .8
            height: dp(46)
            valign: "center"
            md_bg_color: "#FFFFFF"
            pos_hint: {"center_x":.5, "center_y":.5}
            spacing: dp(10)

            MDIcon:
                icon: "plus-circle"
                pos_hint: {"center_x": .5, "center_y": .5}
            MDLabel:
                text:"Base Salary"
                size_hint_x: .4
            MDTextField:
                id:base
                mode: "rectangle"
                input_filter:"int"
                text_color_normal: "#222222"
                line_color_normal: "#222222"
                hint_text: "Base Salary"
                pos_hint: {"center_x": .5, "center_y": .5}
                on_text:
                    root.ids.base_label.text = f"{self.text} JPY"
                    app.update()
            MDLabel:
                id: base_label
                text:" JPY"

        MDBoxLayout:
            size_hint_x: .8
            height: dp(46)
            valign: "center"
            md_bg_color: "#FFFFFF"
            pos_hint: {"center_x":.5, "center_y":.5}
            spacing: dp(10)


            MDIcon:
                icon: "minus-circle"
                pos_hint: {"center_x": .5, "center_y": .5}
                color: "#9d0208"
            MDLabel:
                text:"Health"
                size_hint_x: .4
                color: "#6a040f"
            MDTextField:
                id:health
                mode: "rectangle"
                input_filter:"int"
                hint_text: "% Health"
                pos_hint: {"center_x": .5, "center_y": .5}
                text_color_normal: "#9d0208"
                line_color_normal: "#9d0208"
                on_text:
                    self.text = str(max(0, min(100, int(self.text or 0))))
                    app.update()
            MDLabel:
                id: health_label
                text:" JPY"
                color: "#9d0208"

        MDBoxLayout:
            size_hint_x: .8
            height: dp(46)
            valign: "center"
            md_bg_color: "#FFFFFF"
            pos_hint: {"center_x":.5, "center_y":.5}
            spacing: dp(10)


            MDIcon:
                icon: "minus-circle"
                pos_hint: {"center_x": .5, "center_y": .5}
                color: "#9d0208"
            MDLabel:
                text: "Pension"
                size_hint_x: .4
                color: "#9d0208"
            MDTextField:
                id:pension
                mode: "rectangle"
                input_filter:"int"
                hint_text: "% Pension"
                text_color_normal: "#9d0208"
                line_color_normal: "#9d0208"
                pos_hint: {"center_x": .5, "center_y": .5}
                on_text:
                    self.text = str(max(0, min(100, int(self.text or 0))))
                    app.update()
            MDLabel:
                id: pension_label
                text:" JPY"
                color: "#9d0208"


        MDBoxLayout:
            size_hint_x: .8
            height: dp(46)
            valign: "center"
            md_bg_color: "#FFFFFF"
            pos_hint: {"center_x":.5, "center_y":.5}
            spacing: dp(10)

            MDIcon:
                icon: "minus-circle"
                pos_hint: {"center_x": .5, "center_y": .5}
                color: "#9d0208"
            MDLabel:
                text:"Income Tax"
                size_hint_x: .4
                color: "#9d0208"
            MDTextField:
                id:income_tax
                mode: "rectangle"
                input_filter:"int"
                hint_text: "% Income"
                text_color_normal: "#9d0208"
                line_color_normal: "#9d0208"
                pos_hint: {"center_x": .5, "center_y": .5}
                on_text:
                    self.text = str(max(0, min(100, int(self.text or 0))))
                    app.update()
            MDLabel:
                id: income_tax_label
                text:" JPY"
                color: "#9d0208"

        MDBoxLayout:
            size_hint_x: .8
            height: dp(46)
            valign: "center"
            md_bg_color: "#FFFFFF"
            pos_hint: {"center_x":.5, "center_y":.5}
            spacing: dp(10)


            MDIcon:
                icon: "minus-circle"
                pos_hint: {"center_x": .5, "center_y": .5}
                color: "#9d0208"
            MDLabel:
                text:"Inhabitant Tax"
                size_hint_x: .4
                color: "#9d0208"
            MDTextField:
                id:inhabitant
                mode: "rectangle"
                input_filter:"int"
                hint_text: "%  Income"
                text_color_normal: "#9d0208"
                line_color_normal: "#9d0208"
                pos_hint: {"center_x": .5, "center_y": .5}
                on_text:
                    self.text = str(max(0, min(100, int(self.text or 0))))
                    app.update()
            MDLabel:
                id: inhabitant_label
                text:" JPY"
                color: "#9d0208"


        MDBoxLayout:
            size_hint_x: .8
            height: dp(46)
            valign: "center"
            md_bg_color: "#22223b"
            pos_hint: {"center_x":.5, "center_y":.5}
            spacing: dp(10)

            MDLabel:
                size_hint_x: .5
            MDIcon:
                icon: "calculator"
                pos_hint: {"center_x": .5, "center_y": .5}
                color: "#F2F2F2"
            MDLabel:
                text:"Net Salary"
                size_hint_x: .4
                color: "#F2F2F2"
            MDLabel:
                id: salary_label
                text:" JPY"
                color: "#F2F2F2"
            MDFloatingActionButton:
                icon:"content-save-plus"
                md_bg_color:"#ffc300"
                icon_color:"#222222"
                pos_hint: {"center_x": .5, "center_y": .5}
                on_press:
                    app.save()

            MDFloatingActionButton:
                icon:"autorenew"
                md_bg_color:"#2a9d8f"
                icon_color:"#222222"
                pos_hint: {"center_x": .5, "center_y": .5}
                on_press:
                    app.clear()

        MDBoxLayout:
            size_hint: .8, .2
            valign: "center"
            md_bg_color: "#FFFFFF"
            pos_hint: {"center_x":.5, "center_y":.5}

            MDLabel:
                id: hash
                halign: "center"
                text: "----"
                font_style: "Caption"
```

## 3. Proof of work
![evidence_047_1.png](..%2F..%2Fassets%2Fevidence%2Fevidence_043-050%2Fevidence_047_1.png)
**Fig.3:** Evidence for quiz 047

![evidence_047_2.png](..%2F..%2Fassets%2Fevidence%2Fevidence_043-050%2Fevidence_047_2.png)
**Fig.4:** Evidence for quiz 047

![evidence_047_3.png](..%2F..%2Fassets%2Fevidence%2Fevidence_043-050%2Fevidence_047_3.png)
**Fig.5:** Evidence for quiz 047

![evidence_047.gif](..%2F..%2Fassets%2Fevidence%2Fevidence_043-050%2Fevidence_047.gif)
**Fig.6:** Evidence for quiz 047 (video)
