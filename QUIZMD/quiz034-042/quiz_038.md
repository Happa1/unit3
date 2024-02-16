# Quiz 038
![quiz_038.jpg](..%2Fassets%2Fprompt%2Fquiz_038.jpg)
**Fig.1:** prompt of quiz 038

## 1. flow of chart
![quiz_diagram_038.jpg](..%2Fassets%2Fflowchart%2Fquiz_diagram_038.jpg)
**Fig.2:** algorithm flow chart of quiz 038

## 2. solution
```.py
import random
from matplotlib import pyplot as plt

class SalesmanMap():
    def __init__(self):
        self.x = None
        self.y = None
        self.name = None

    def get_map(self):
        plt.scatter(self.x,self.y, marker='o', c='red')
        for i, label in enumerate(self.name):
            plt.annotate(label, (self.x[i], self.y[i]))

        plt.show()

    def generate_data(self,names:list[str]):
        self.x = [random.randint(0,100) for i in range(len(names))]
        self.y = [random.randint(0,100) for i in range(len(names))]
        self.name= names

test = SalesmanMap()
test_data = test.generate_data(['Kyoto', 'Osaka','Kobe','Nara'])
test.get_map()

```

## 3. Proof of work
![evidence_038.png](..%2Fassets%2Fevidence%2Fevidence_038.png)
**Fig.3:** Evidence for quiz 038