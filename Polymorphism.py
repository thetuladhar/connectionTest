class Vehicle:

    def display(self):
        print("Showing vehicle information")

class Car(Vehicle):
    #method Overriding 
    def __init__(self, speed=100):
        self.speed= speed

    def display(self):
        print("Showing vehicle information.")
        print("Speed is",self.speed)

class Truck(Vehicle):

    def __init__(self, speed=100):
        self.speed= speed

car1=Car()
#car1.display()

truck1=Truck()
Truck.display()