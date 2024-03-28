# Quiz 055
![quiz_055.jpg](..%2F..%2Fassets%2Fprompt%2Fquiz_050-056%2Fquiz_055.jpg)
**Fig.1:** prompt of quiz 055

## 1. flow of chart
![quiz_diagram_055.jpg](..%2F..%2Fassets%2Fflowchart%2Fflowchart_051-056%2Fquiz_diagram_055.jpg)
**Fig.2:** algorithm flow chart of quiz 055

## 2. solution
```.py
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
```

## 3. Proof of work
![evidence_055.png](..%2F..%2Fassets%2Fevidence%2Fevidence_051-056%2Fevidence_055.png)
**Fig.3:** Evidence for quiz 055