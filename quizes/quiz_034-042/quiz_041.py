from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.button import MDFlatButton
import random

class MyButton(MDFlatButton):
    pass
class quiz_041(MDApp):
    def build(self):
        Window.size = (500,500)
        pass
    def button_pressed(self, btn):
        n = random.randint(0, 1)
        if n ==0:
            btn.text = "O"
            btn.md_bg_color ="#fffdd0"
            btn.bold = True
            btn.font_size = "15pt"
        else:
            btn.text = "X"
            btn.md_bg_color = "#bb011b"
            btn.bold = True
            btn.font_size = "15pt"

test = quiz_041()
test.run()