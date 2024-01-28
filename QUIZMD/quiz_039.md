# Quiz 039
![quiz_039.jpg](..%2Fassets%2Fprompt%2Fquiz_039.jpg)
**Fig.1:** prompt of quiz 039

## 1. flow of chart
![quiz_diagram_039.jpg](..%2Fassets%2Fflowchart%2Fquiz_diagram_039.jpg)
**Fig.2:** algorithm flow chart of quiz 039

## 2. solution
```.py
from kivymd.app import MDApp

class quiz_039(MDApp):
    def build(self):
        self.count = 0
        return

    def button_pressed(self):
        label = self.root.ids.my_btn
        self.count += 1
        label.text = f"Count {self.count}"
        label.color = "red"

text = quiz_039()
text.run()
```

```.kv
Screen:
    size: 500, 500

    MDBoxLayout:
        orientation: "horizontal"
        size_hint: 0.7, .3
        pos_hint: {"center_x":.5, "center_y":.5}

        MDLabel:
            id: my_btn
            text: "Count"
            size_hint: 0.5, 1
            font_size: "34pt"
            halign: "center"
            color: "red"
            md_bg_color: "#63e5ff"


        MDRaisedButton:
            text: "Add + 1"
            size_hint: 0.5, 1
            pos_hint: {"center_x":.5, "center_y":.5}
            font_size: "34pt"
            md_bg_color: "#000000"
            on_press:
                app.button_pressed()
```

## 3. Proof of work
![evidence_039.png](..%2Fassets%2Fevidence%2Fevidence_039.png)
**Fig.3:** Evidence for quiz 039