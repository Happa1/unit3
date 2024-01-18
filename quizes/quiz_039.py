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