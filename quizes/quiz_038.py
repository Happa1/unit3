import random
from matplotlib import pyplot as plt

class SalesmanMap():
    def __init__(self):
        self.x = None
        self.y = None
        self.name = None

    def get_map(self):
        # self.x = x
        # self.y = y
        # self.name = name
        plt.scatter(self.x,self.y, marker='o', c='red')
        for i, label in enumerate(self.name):
            plt.annotate(label, (self.x[i], self.y[i]))

        plt.show()

    def generate_data(self,names:list[str]):
        self.x = [random.randint(0,100) for i in range(len(names))]
        self.y = [random.randint(0,100) for i in range(len(names))]
        self.name= names

test = SalesmanMap()
test_data = test.generate_data(['Kyoto', 'Osak','Kobe','Nara'])
test.get_map()

