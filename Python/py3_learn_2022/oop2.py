from pyexpat import model
from turtle import color
from car import Car

car_1 = Car("Chevy","Corvette",2021,"blue")
car_2 = Car("Mercedes","Benz",2022,"Silver")


print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)
print(car_1.wheels)

car_1.drive()
car_1.stop()
