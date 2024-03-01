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