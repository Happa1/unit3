# Quiz 035
![quiz_035.jpg](..%2F..%2Fassets%2Fprompt%2Fquiz_034-042%2Fqu iz_035.jpg)
![quiz_035_2.jpg](..%2F..%2Fassets%2Fprompt%2Fquiz_034-042%2Fquiz_035_2.jpg)
**Fig.1:** prompt of quiz 035

## 1. flow of chart
![quiz_diagram_035.jpg](..%2F..%2Fassets%2Fflowchart%2Fflowchart_034-042%2Fquiz_diagram_035.jpg)
**Fig.2:** algorithm flow chart of quiz 035

## 2. solution
```.py
class Converter:
    def __init__(self):
        self.roman_symbols = {
            100: 'C',
            90 : 'XC',
            50: 'L',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'
        }

    def convert_to_roman(self, decimal:int) -> str:
        if decimal > 0 and decimal < 101:
            output=''
            for k,v in self.roman_symbols.items():
                q = decimal//k
                output += q*v
                decimal = decimal%k
            return  output
        else:
            return  "Please enter the number between 1 and 100"


test = Converter().convert_to_roman(decimal=20)
print(test)

```

## 3. Proof of work
![evidence_035.png](..%2F..%2Fassets%2Fevidence%2Fevidence_034-042%2Fevidence_035.png)
**Fig.3:** Evidence for quiz 035