# Quiz 034
![quiz_034.jpg](..%2Fassets%2Fprompt%2Fquiz_034.jpg)
**Fig.1:** prompt of quiz 034

## 1. flow of chart
![quiz_diagram_034.jpg](..%2Fassets%2Fflowchart%2Fquiz_diagram_034.jpg)
**Fig.2:** algorithm flow chart of quiz 034

## 2. solution
```.py
def mystery (list1:list, list2:list) -> list:
    output=[]
    for k,v in zip(list1,list2):
        if list1[k] == list2[v]:
            output.append(list1[k])
    return output

test = mystery([1,2,3,4,5,6,7], [2,2,3,4,5,5])
print(test)
```

## 3. Proof of work
![evidence_034.png](..%2Fassets%2Fevidence%2Fevidence_034.png)
**Fig.3:** Evidence for quiz 034