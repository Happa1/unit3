from kivy.config import Config
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '600')

from kivymd.app import MDApp
class MyCalculator(MDApp):
    def build(self):
        self.count = '0'
        self.cal = 0
        self.method_type = None
        self.is_refresh = False
        return

    def press_number(self, instance):
        self.number_display(instance.text)

    def number_display(self, number):
        if self.count == '0':
            self.count = number
        elif self.is_refresh:
            self.count = number
            self.is_refresh = False
        else:
            self.count += number
        label = self.root.ids.label_num
        label.text = self.count


    def is_all_set(self):
        return self.cal and self.method_type

    def calculate(self):
        if self.method_type == "+":
            return float(self.cal) + float(self.count)
        elif self.method_type == "-":
            return float(self.cal) - float(self.count)
        elif self.method_type == "×":
            return float(self.cal) * float(self.count)
        elif self.method_type == "÷":
            return float(self.cal) / float(self.count)
        elif self.method_type == "=":
            return self.cal



    def call_method(self, method):
        if not self.cal and method != '=': #何も入力していない状態で、メソッドボタンを押した時
            self.cal = float(self.count)
            self.method_type = method
            self.is_refresh = True
            print(f'1 {self.cal}')


        elif self.is_all_set and method == '=': #=を押した時
            value = self.calculate()
            self.cal = value
            if value.is_integer():
                value = int(value)
                self.count = str(value)
            else:
                self.count = str(value)
            self.method_type = method
            self.is_refresh = True
            print(f'2 {self.cal}, {method},{self.count}')


        elif self.is_all_set and method != '=': #続けて計算するとき
            value = self.calculate()
            self.cal = value
            if value.is_integer():
                value = int(value)
                self.count = str(value)
            else:
                self.count = str(value)
            self.method_type = method
            self.is_refresh = True
            print(f'3 {self.cal}, {method} {self.count}')

        label = self.root.ids.label_num
        label.text = self.count
        text = label.text
        if len(text) > 10:
            label.text = text[:10]


    def press_function(self, instance):
        function = instance.text
        if function == "+/-":
            if self.method_type == "=":
                value = float(self.count) * (-1)
                self.cal = value
            else:
                value = float(self.count) * (-1)
        elif function == "%":
            if self.method_type == "=":
                value = float(self.count)*0.01
                self.cal = value
            else:
                value = float(self.count)*0.01

        if value.is_integer():
            value = int(value)
            self.count = str(value)
        else:
            self.count = str(value)
        label = self.root.ids.label_num
        label.text = self.count



    def clear_all(self):
        label = self.root.ids.label_num
        self.count = '0'
        label.text = self.count
        self.cal = None
        self.methodtype = None
        self.is_refresh = False



test = MyCalculator()
test.run()