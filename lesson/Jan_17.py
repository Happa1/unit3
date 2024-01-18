import random
import string
class Engine:
    def __init__(self, fuel_type, size:int):
        self.fuel_type = fuel_type
        if self.fuel_type == 'Gasoline':
            self.size = str(size) + "L"
        else:
            self.size = str(size) + "kW/h"

    def start(self):
        print("Engine started")

    def stop(self):
        print("Engine stopped")

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.engine = None

    def set_engine(self,engine):
        self.engine= Engine()

    def start(self):
        if self.engine:
            print(f"{self.brand} {self.model}'s engine is starting")
            self.engine.start()
        else:
            print("No engine set for the vehicle")

    def stop(self):
        if self.engine:
            print(f"{self.brand} {self.model}'s engine is stopping")
            self.engine.stop()
        else:
            print("No engine set for the vehicle")

class Car(Vehicle):
    def __init__(self, brand, model, num_doors, no_passenger):
        super().__init__(brand,model)
        self.num_doors = num_doors
        self.no_passenger = no_passenger

    def add_passengers(self, passenger):
        current_passenger = self.no_passenger
        fit = False
        if current_passenger + passenger <= 4:
            fit = True

        if fit == True:
            self.no_passenger= current_passenger + passenger
            print(f'{current_passenger + passenger} people can fit the car.')
        else:
            print(f'{current_passenger + passenger} people cannot fit the car.')

    def remove_passenger(self, passenger):
        current_passenger = self.no_passenger
        removed = current_passenger - passenger
        self.no_passenger = removed
        print(f'{removed} people are in the car.')

class LicensePlate(Vehicle):
    def __init__(self,brand, model, num_doors, no_passenger):
        super().__init__(brand, model)
        self.licenseplate = None

    def set_licenseplate(self):
        letter = chr(random.randint(ord('あ'),ord('ん')))
        first_no = [str(random.randint(0,9) for _ in range(3))]
        second_no = [str(random.randint(0,9) for _ in range(2))]
        self.licenseplate = letter + ''.join(first_no) + '-' + ''.join(second_no)

        return f'Your license plate number is {self.licenseplate}'

#Example Usage:
gasoline_engine = Engine("Gasoline", 10) # Create an engine
my_car = Car("Toyota", "Camry",4,3) # Create a car and set its engine
my_car.set_engine(gasoline_engine)

car_2 = LicensePlate("Mitsubishi", "aaa",6,4)
lisence = car_2.set_licenseplate()
print(lisence)

electronic_engine=Engine("Electric",30)
i_miev=Car("Mitsubishi", "i_MiEV",4,3)


#Start and stop the car
my_car.start()
my_car.start()