class CompoundInterest:
    def __init__(self, principal:int, rate:float, number_of_years:int):
        self.principal = principal
        self.rate = rate
        self.number_of_years = number_of_years

    def calculate(self):
        self.current_money = self.principal*(1+self.rate)**self.number_of_years
        return self.current_money

    def get_rate(self):
        return self.rate

class AccountingProgram(CompoundInterest):
    def __init__(self, principal, rate, number_of_years, customer_name):
        super().__init__(principal, rate, number_of_years) # CompoundInterestで引き継いだ値はこっちでも使う。
        self.customer_name = customer_name
        self.customer_email = None


    def get_message(self):
        return f'{self.customer_name} will have {self.current_money} USD in {self.number_of_years} if the principa; is {self.principal} with {self.rate} %.'

    def get_email(self, domain):
        return f'{self.customer_name}`{domain}'

manaha = AccountingProgram(principal=100, rate=0.1, number_of_years=1,customer_name='Manaha')
calculation = manaha.calculate()
print(calculation)
rate = manaha.get_rate()
print(rate)
message = manaha.get_message('Manaha')
print(message)
email = manaha.get_email('uwciksa.jp')
print(email)



