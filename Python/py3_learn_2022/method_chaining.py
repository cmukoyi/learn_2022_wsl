
class Car:

    def turn_on(self):
        print("You start the engine")
        return(self)    
    
    def drive(self):
        print("you drive the car")
        return(self)
    
    def brake(self):
        print("Car brakes")
        return(self)

car = Car()

car.turn_on()\
   .brake()\
    .drive()
    