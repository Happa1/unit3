# Quiz 056
![quiz_056.jpg](..%2F..%2Fassets%2Fprompt%2Fquiz_050-056%2Fquiz_056.jpg)
**Fig.1:** prompt of quiz 056

## 1. flow of chart
![quiz_diagram_056.jpg](..%2F..%2Fassets%2Fflowchart%2Fflowchart_051-056%2Fquiz_diagram_056.jpg)
**Fig.2:** algorithm flow chart of quiz 056

## 2. solution
```.py
code = int(input("please enter the number between 1 - 31"))
binary =''

while code!=0:
    left = str (code%2)
    code = code//2
    binary+=left

binary = int(binary[::-1])

action_d ={1:"wink", 10: "double blink", 100: "close your eyes", 1000: "jump"}
digit=0
out=[]

while binary!=0:
    remain = binary % 10
    binary = binary//10
    action_num = remain*10**digit
    digit+=1
    if action_num in action_d:
        out.append(action_d[action_num])
    if action_num == 10000:
        out.reverse()

print(out)
```

## 3. Proof of work
![evidence_056.png](..%2F..%2Fassets%2Fevidence%2Fevidence_051-056%2Fevidence_056.png)
**Fig.3:** Evidence for quiz 056