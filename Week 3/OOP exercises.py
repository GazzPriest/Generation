class Vehicle:
    def __init__(self, max_speed, colour):
        self.max_speed = max_speed
        self.colour = colour

    def car_info(self):
        print("This car goes {} mph and is {}".format(self.max_speed, self.colour))
    
    def change_max_speed(self): #3
        self.max_speed += 20 
    
    def change_colour(self): #3
        self.colour = 'Black'

Ferrari = Vehicle(200, 'Red')   #2

Ferrari.car_info()
Ferrari.change_max_speed()
Ferrari.change_colour()
Ferrari.car_info()

############################################################

class Bus(Vehicle): #4
    def __init__(self, max_speed, colour, seating_capacity):
        super().__init__(max_speed, colour)
        self.capacity = seating_capacity

    def bus_fare(self):
        print((self.capacity * 0.05) + ((self.capacity * 0.05) * 1.1))

    def __repr__(self):
        return f'Max Speed: {self.max_speed}, Colour: {self.colour}, Seating Capacity: {self.capacity}'

SchoolBus = Bus(120, 'White', 40)

print(type(Bus)) #5

print(isinstance(SchoolBus, Vehicle)) #6

SchoolBus.bus_fare() #7

print(repr(SchoolBus)) #8