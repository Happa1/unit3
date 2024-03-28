# Quiz 053
![quiz_053.jpg](..%2F..%2Fassets%2Fprompt%2Fquiz_050-056%2Fquiz_053.jpg)
**Fig.1:** prompt of quiz 053

## 1. flow of chart
![quiz_diagram_053.jpg](..%2F..%2Fassets%2Fflowchart%2Fflowchart_051-056%2Fquiz_diagram_053.jpg)
**Fig.2:** algorithm flow chart of quiz 053

## 2. solution
```.py
class palNum:
    def __init__(self, A, B):
        self.A = A
        self.B = B

    def palindromic_numbers(self):
        a = self.A
        b = self.B
        out = []
        for i in range (a, b+1):
            str_num = str(i)
            reverse_num = ''
            for l in str_num:
                reverse_num = l + reverse_num
                if str_num == reverse_num:
                    out.append(i)
        return out


    def palindromic_numbers_2(self):
        a = self.A
        b = self.B
        out = []

        for i in range (a, b+1):
            str_num = str(i)
            reverse_num = ''
            for l in range(0, len(str_num), -1):
                print(l)
                reverse_num += str_num[l]
                if str_num == reverse_num:
                    out.append(i)
        return out


test = palNum(11,199)
get_num = test.palindromic_numbers()
print(get_num)

get_num_2 = test.palindromic_numbers_2()
print(get_num_2)

```

## 3. Proof of work
![evidence_053.png](..%2F..%2Fassets%2Fevidence%2Fevidence_051-056%2Fevidence_053.png)
**Fig.3:** Evidence for quiz 053