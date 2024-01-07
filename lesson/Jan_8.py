## OOP class and object
# January 8th

class Paraglider:
    def __init__(glider,my_size,my_color,my_weight,my_price): #you can change self to glider
        glider.size = my_size
        glider.color = my_color
        glider.weight = my_weight
        glider.price = my_price

    def get_color(glider): # this function is inside the class and called 'Method'
        return f"This glider's color is {glider.color} JPY"

    def get_price(glider):
        return glider.price

    def set_price(glider, new_price):
        glider.price = new_price


# create an object of the class Paraglider
# create an instance of the class Paraglider
spor_glider = Paraglider(my_size='L',my_color='blue',my_weight=3,my_price=300000)
leisure_glider = Paraglider(my_size='M',my_color='red',my_weight=8,my_price=250000)

print(spor_glider.get_color())
print(Paraglider.get_color(leisure_glider))

old_price = spor_glider.get_price()
spor_glider.set_price(new_price=1.1*old_price)
print(spor_glider.get_price())

