# Quiz 041
![quiz_041.jpg](..%2Fassets%2Fprompt%2Fquiz_041.jpg)
**Fig.1:** prompt of quiz 041

## 1. flow of chart

**Fig.2:** algorithm flow chart of quiz 041

## 2. solution

### python code
```.py
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
```

### kivy code
```.kv
Screen:
    size: 500,500

    MDBoxLayout:
        size_hint: .8, .8
        pos_hint: {"center_x":.5, "center_y":.5}
        orientation:"vertical"

        MDLabel:
            size_hint: 1, .1
            pos_hint: {"center_x":.5, "center_y":.5}
            text: "Tic Tac Toe by student_name"
            font_size: "24pt"
            halign: "center"

        MDLabel:
            size_hint: 1, .1
            pos_hint: {"center_x":.5, "center_y":.5}
            text: "It is X's turn"
            bold: True
            font_size: "15pt"
            halign: "center"

        MDBoxLayout:
            size_hint: 1, .7
            orientation: "vertical"
            padding: dp(2)

            MDBoxLayout:
                orientation:"horizontal"
                size_hint: 1,.25
                color: "white"
                md_bg_color:"white"
                MyButton:
                MyButton:
                MyButton:

            MDBoxLayout:
                orientation:"horizontal"
                size_hint: 1,.25
                md_bg_color:"white"
                MyButton:
                MyButton:
                MyButton:

            MDBoxLayout:
                orientation:"horizontal"
                size_hint: 1,.25
                md_bg_color:"white"
                MyButton:
                MyButton:
                MyButton:

<MyButton>:
    size_hint: 1,1
    padding: dp(2)
    MDFlatButton:
        size_hint: 1,1
        md_bg_color:"#7ebea5"
        padding: dp(2)
        on_press:
            app.button_pressed(self)
```

## 3. Proof of work
![evidence_041.png](..%2Fassets%2Fevidence%2Fevidence_041.png)
**Fig.3:** Evidence for quiz 041