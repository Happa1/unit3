# quiz36
class Account:
    def __init__(self):
        self.balance = 0
        self.holder_name = ""
        self.holder_email = ""
        self.number = ['000','00000','0']

    def get_account_no(self) -> str:
        output = f"{self.number[0]}-{self.number[1]}-{self.number[2]}"
        return output

    def set_holer_name(self, name:str) -> str:
        self.holder_name = name
        return f"Holder's name is {self.holder_name.title()}"

    def set_holder_email(self, email:str) -> str:
        self.holder_email = email
        return f"Holder's email is {self.holder_email}"

    def get_balance(self)->int:
        return self.balance

    def deposit(self, amount:int) -> str:
        self.balance += amount
        return f"New balance: {Account.get_balance(self)} USD"

test = Account()
holder_name = test.set_holer_name("Yuko")
print(test.holder_name)