# Quiz 054
![quiz_054.jpg](..%2F..%2Fassets%2Fprompt%2Fquiz_050-056%2Fquiz_054.jpg)
**Fig.1:** prompt of quiz 054

## 1. flow of chart
![quiz_diagram_054.jpg](..%2F..%2Fassets%2Fflowchart%2Fflowchart_051-056%2Fquiz_diagram_054.jpg)
**Fig.2:** algorithm flow chart of quiz 054

## 2. solution
```.py
class rainDrops:
    def __init__(self,n):
        self.n = n

    def pour(self):
        n= self.n
        rain = {3:'i', 5:'a',7:'o'}
        out = [f'Pl{v}ng'*(n%k==0) for k,v in rain.items()]
        return ''.join(out) or str(n)


    # def pour_2(self):
    #     rain = {3:'i', 5:'a',7:'o'}
    #     out = filter(lambda x=d: self%d==0, [f"Pl{r}ng" for d,r in rain])


test = rainDrops(30)
print(test.pour())
```

## 3. Proof of work
![evidence_054.png](..%2F..%2Fassets%2Fevidence%2Fevidence_051-056%2Fevidence_054.png)
**Fig.3:** Evidence for quiz 054