# Quiz 042

**Fig.1:** prompt of quiz 042

## 1. flow of chart

**Fig.2:** algorithm flow chart of quiz 042

## 2. solution
### python code
```.py
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen

class FirstScreen(MDScreen):
    def try_change(self):
        self.parent.current = "MysteryPageB"
class SecondScreen(MDScreen):
    def try_change(self):
        self.parent.current = "MysteryPageA"
class quiz_042(MDApp):
    def build(self):
        Window.size = (400, 700)

    def changed(self):
        pass


t = quiz_042()
t.run()
```

### kivy code
```.kv
ScreenManager:
    FirstScreen:
        name: "MysteryPageA"
    SecondScreen:
        name: "MysteryPageB"

<FirstScreen>:
    MDLabel:
        text: "This is mystery page A you pressed the button"
        halign: "center"

    MDFloatingActionButton:
        size_hint: .3,.1
        pos_hint: {"center_x":.5, "center_y":.3}
        style: "standard"
        md_bg_color: "#0092ff"
        on_press:
            root.try_change()
            app.changed()

<SecondScreen>:
    MDLabel:
        text: "This is mystery page B you pressed the button"
        halign: "center"

    MDFloatingActionButton:
        size_hint: .3,.1
        pos_hint: {"center_x":.5, "center_y":.3}
        style: "standard"
        md_bg_color: "#0092ff"
        on_press:
            root.try_change()
            app.changed()
```

## 3. Proof of work
![evidence_042.png](..%2Fassets%2Fevidence%2Fevidence_042.png)
**Fig.3:** Evidence for quiz 042