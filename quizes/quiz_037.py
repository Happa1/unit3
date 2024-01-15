class CompoundInterest:
    def __init__(self):
        self.principal = None
        self.rate =  None
        self.number_of_years = None

    def calculate(self, principal, rate, number_of_years):
        self.principal = principal
        self.rate = rate
        self.number_of_years = number_of_years
        self.current_money = self.principal*(1+self.rate)**self.number_of_years
        return self.current_money

    def get_rate(self):
        return self.rate

class Accounting(CompoundInterest):
    # def __init__(self):
    #     # super(Accounting,self).__init__(self)
    #     self.customer_name = None
    #     self.customer_email = None

    def get_rate2(self):
        return self.rate
    def get_message(self, customer_name):
        self.customer_name = customer_name
        return f'{self.customer_name} will have {self.current_money} USD in {self.number_of_years} if the principa; is {self.principal} with {self.rate} %.'

manaha = CompoundInterest()
calculation = manaha.calculate(principal=100, rate=0.1, number_of_years=1)
print(calculation)
rate = manaha.get_rate()
print(rate)
rate2 = manaha.get_rate2()
print(rate2)
message = manaha.get_message('Manaha')
print(message)



