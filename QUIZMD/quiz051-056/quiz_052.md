# Quiz 052
![quiz_052.jpg](..%2F..%2Fassets%2Fprompt%2Fquiz_050-056%2Fquiz_052.jpg)
**Fig.1:** prompt of quiz 052

## 1. flow of chart
![quiz_diagram_052.jpg](..%2F..%2Fassets%2Fflowchart%2Fflowchart_051-056%2Fquiz_diagram_052.jpg)
**Fig.2:** algorithm flow chart of quiz 052

## 2. solution
```.py
import math
class Wheels:
    def __init__(self, size):
        self.size = size

    def get_size(self):
        return self.size

    def get_perimeter(self):
        perimeter = 2 * math.pi * self.size
        return perimeter

    def get_km_per_rotation(self):
        in_km = self.size * 2.54 * 10 ** (-4)
        return f'per rotation is {in_km}km'


class Bicycle:
    def __init__(self, material, size):
        self.material = material
        self.my_size = Wheels(size).size

    def ride(self):
        out = f"This is a bicycle with wheel size {self.my_size} and frame {self.material}."
        return out



test = Bicycle('aluminum', 26)
print(test.ride())

test2=Wheels(26)
print(test2.get_perimeter())
print(test2.get_size())
print(test2.get_km_per_rotation())
```

## 3. Proof of work
![evidence_052.png](..%2F..%2Fassets%2Fevidence%2Fevidence_051-056%2Fevidence_052.png)
**Fig.3:** Evidence for quiz 052