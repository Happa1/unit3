# Quiz 040
![quiz_040.jpg](..%2Fassets%2Fprompt%2Fquiz_040.jpg)
**Fig.1:** prompt of quiz 040

## 1. flow of chart

**Fig.2:** algorithm flow chart of quiz 040

## 2. solution

### python code
```.py
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen

class FirstScreen(MDScreen):
    def try_change(self):
        self.parent.current = "Second"
class SecondScreen(MDScreen):
    pass
class quiz_040(MDApp):
    def build(self):
        Window.size = (400,700)
    def changed(self):
        print("page was changed")

t = quiz_040()
t.run()
```

### kivy code
```.kv
ScreenManager:
    FirstScreen:
        name:"First"

    SecondScreen:
        name: "Second"

<FirstScreen>:
    MDLabel:
        text: "This is the First Screen"
    MDFloatingActionButton:
        icon: "pencil-outline"
        style: "standard"
        on_press:
            root.try_change()
            app.changed()

<SecondScreen>:
    MDLabel:
        text: "This is the Second Screen"
    MDFloatingActionButton:
        icon: "pencil-outline"
        style: "standard"
        on_press:
            root.parent.current = "First"

```

## 3. Proof of work
![evidence_040_1.png](..%2Fassets%2Fevidence%2Fevidence_040_1.png)
![evidence_040_2.png](..%2Fassets%2Fevidence%2Fevidence_040_2.png)
**Fig.3:** Evidence for quiz 040