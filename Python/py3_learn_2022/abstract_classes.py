from abc import ABC, abstractmethod

@abstractmethod
class Vehicle(ABC):
    def go(self):
        pass

class Car(Vehicle):

    def go(self):
        print("You drive the car")

class Motorcycle(Vehicle):

    def go(self):
        print("You ride a bike")


vehicle = Vehicle()

car = Car()
car.go()
vehicle.go()