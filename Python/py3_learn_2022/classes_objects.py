#pass objects are arguments 

class Car:
    color = None

class Bike:
    color = None

def change_color(car,color):
    
    car.color = color

car_1 = Car()
car_2 = Car()
car_3 = Car()
bike_1 = Bike()

change_color(car_1,"Blue")
change_color(car_2,"red")
change_color(car_3,"White")
change_color(bike_1,"Silver")


print(car_1.color)
print(car_2.color)
print(car_3.color)
print(bike_1.color)
