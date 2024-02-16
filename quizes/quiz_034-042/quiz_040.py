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