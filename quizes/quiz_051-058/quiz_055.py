class darts:
    def __init__(self, x, y):
        self.x=x
        self.y=y

    def calculate(self):
        num_x=self.x
        num_y=self.y
        score = 0
        if 5**2 < num_x**2 + num_y** 2 <=10**2:
            score+=1

        if 1**2 < num_x**2 + num_y** 2 <=5**2:
            score+=5

        if num_x**2 + num_y** 2 <=1**2:
            score+=10

        return score


test=darts(x=3, y=8)
print(test.calculate())