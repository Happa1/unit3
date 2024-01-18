# example1.py
from kivymd.app import MDApp

class my_first_app(MDApp):
    def build(self):
        return

    def button_pressed(self):
        label = self.root.ids.my_label
        label.text = "The button was pressed"
        label.color = "red"
        btn = self.root.ids.my_btn

        if btn.md_bg_color == [0,0,1,1]:
            btn.md_bg_color = "#FF0033"
        else:
            btn.md_bg_color = "blue"

text = my_first_app()
text.run()