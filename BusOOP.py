class Vehicle:
    def __init__(self,vehicle,seats):
        self.vehicle=vehicle
        self.seats=seats
    def fare(self):
        return self.seats*100

class Car(Vehicle):
    def __init__(self,cartype):
        print("Type is Car")
        super().__init__(cartype,seats=5)

class Bus(Vehicle):
    def __init__(self):
        super().__init__("Bus",seats=50)
    
    def fare(self):
        base=super().fare()
        maintenance=0.10* base
        total=base+maintenance
        return total

instance = Car("Sedan")
FinalFare=instance.fare()

print("Final Fare for",instance.vehicle,"is",FinalFare )

