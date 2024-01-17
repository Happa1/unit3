class Engine:
    def __init__(self, fuel_type, size):
        self.fuel_type = fuel_type
        self.size = size

    def start(self):
        print("Engine started")

    def stop(self):
        print("Engine stopped")

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.engine = None

    def set_engine(self, engine:Engine):
        self.engine= engine

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
        if current_passenger + passenger < 4:
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
    def __init__(self,brand, model, num_doors, no_passenger,licenseplate):
        super().__init__(brand, model, num_doors, no_passenger)
        self.licenseplate = licenseplate

    def set_licenseplate(self, license_no):



#Example Usage:
gasoline_engine = Engine("Gasoline") # Create an engine
my_car = Car("Toyota", "Camry",4) # Create a car and set its engine
my_car.set_engine(gasoline_engine)

electronic_engine=Engine("Electric")
i_miev=Car("Mitsubishi", "i_MiEV",4)


#Start and stop the car
my_car.start()
my_car.start()