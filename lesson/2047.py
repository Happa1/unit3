from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout


class MyButton(MDBoxLayout):
    pass


class Game(MDApp):
    def build(self):
        Window.size = (500,700)
    pass

test = Game()
test.run()