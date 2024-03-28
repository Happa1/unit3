# Quiz 051
![quiz_051.jpg](..%2F..%2Fassets%2Fprompt%2Fquiz_050-056%2Fquiz_051.jpg)
**Fig.1:** prompt of quiz 051

## 1. flow of chart
![quiz_diagram_051.jpg](..%2F..%2Fassets%2Fflowchart%2Fflowchart_051-056%2Fquiz_diagram_051.jpg)
**Fig.2:** algorithm flow chart of quiz 051

## 2. solution
```.py
class Aircraft:
    def __init__(self, model, capacity):
        self.model = model
        self.capacity = capacity

    def get_info(self):
        model = self.model
        capacity = self.capacity
        out = f"{model} (Capacity:{capacity})"
        return out


class Flight(Aircraft):
    def __init__(self, model:str, capacity:str, flight_numbers:str, origin:str, destination:str, demonstrate_time:str, duration=list[int]):
        super().__init__(model,capacity)
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

    def get_info(self):
        out=f"Flight {self.flight_numbers} from {self.origin} to {self.destination} departs at {self.demonstrate_time} Aircraft: {self.model} (Capacity: {self.capacity})"
        return out

    # def print_object(self,x):
    #     if x == Aircraft:
    #         return Aircraft.get_info()
    #
    #     elif x == Flight:
    #         return Flight.get_info()

test = Flight(flight_numbers='AA123', origin="New York", destination="Los Angeles", demonstrate_time="10:00AM", duration=[5,30,3], model='AA', capacity=150)
print(test.get_duration())

test2 = Flight(flight_numbers='B777', origin="Tokyo", destination="Fukuoka", demonstrate_time="2:00PM", duration=[1,40,5],  model='AAA', capacity=150)
print(test2.get_duration())

test3 = Aircraft(model='AA', capacity=150)

# print(Flight.print_object(x=test))
print(test.get_info())
print(test3.get_info())
```

## 3. Proof of work
![evidence_051.png](..%2F..%2Fassets%2Fevidence%2Fevidence_051-056%2Fevidence_051.png)
**Fig.3:** Evidence for quiz 051