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

    def print_object_info(obj):
        if isinstance(obj, Aircraft):
            return obj.get_info()
        elif isinstance(obj, Flight):
            return obj.get_info()

test = Flight(flight_numbers='AA123', origin="New York", destination="Los Angeles", demonstrate_time="10:00AM", duration=[5,30,3], model='AA', capacity=150)
print(test.get_duration())

test2 = Flight(flight_numbers='B777', origin="Tokyo", destination="Fukuoka", demonstrate_time="2:00PM", duration=[1,40,5],  model='AAA', capacity=150)
print(test2.get_duration())

test3 = Aircraft(model='AA', capacity=150)

print(test.get_info())
print(test3.get_info())
print(test2.print_object_info())