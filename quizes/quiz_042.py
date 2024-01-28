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