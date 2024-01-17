import random
from matplotlib import pyplot as plt

class SalesmanMap():
    def __init__(self):
        self.x = None
        self.y = None
        self.name = None

    def get_map(self, x:list[int], y:list[int], name:list[str]):
        self.x = x
        self.y = y
        self.name = name
        plt.scatter(x,y, marker='o', c='red')
        for i, label in enumerate(name):
            plt.annotate(label, (x[i], y[i]))

        plt.show()

    def generate_data(self,names:list[str]):
        self.x = [random.randint(0,100) for i in range(names)]
        self.y = [random.randint(0,100) for i in range(names)]
        self.name= names

test = SalesmanMap()
test_data = test.generate_data(['Kyoto', 'Osak','Kobe','Nara'])


