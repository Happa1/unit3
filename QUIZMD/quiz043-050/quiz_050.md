# Quiz 050
![quiz_050.jpg](..%2F..%2Fassets%2Fprompt%2Fquiz_043-050%2Fquiz_050.jpg)
**Fig.1:** prompt of quiz 050

## 1. flow of chart
![quiz_diagram_050.jpg](..%2F..%2Fassets%2Fflowchart%2Fflowchart_043-050%2Fquiz_diagram_050.jpg)
**Fig.2:** UML diagram of quiz 050

## 2. solution
```.py
class Flight:
    def __init__(self, flight_numbers:str, origin:str, destination:str, demonstrate_time:str, duration=list[int]):
        self.flight_numbers = flight_numbers
        self.origin = origin
        self.destination = destination
        self.demonstrate_time = demonstrate_time
        self.duration=duration


    def get_duration(self):
        hour = self.duration[0]
        minute = self.duration[1]
        second = self.duration[2]
        out = f"{hour} hours {minute} minutes and {second} seconds"
        return out

test = Flight(flight_numbers='AA123', origin="New York", destination="Los Angeles", demonstrate_time="10:00AM", duration=[5,30,3])
print(test.get_duration())

test2 = Flight(flight_numbers='B777', origin="Tokyo", destination="Fukuoka", demonstrate_time="2:00PM", duration=[1,40,5])
print(test2.get_duration())

```

## 3. Proof of work
![evidence_050.png](..%2F..%2Fassets%2Fevidence%2Fevidence_043-050%2Fevidence_050.png)
**Fig.3:** Evidence for quiz 050