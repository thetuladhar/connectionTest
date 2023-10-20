class Vehicle:
    def __init__(self,vehicle,seats):
        self.vehicle=vehicle
        self.seats=seats
    def fare(self):
        return self.seats*100

class Car(Vehicle):
    def __init__(self,cartype,seats):
        print("Type is Car")
        super().__init__(cartype,seats)

class CityRide(Car):
    def __init__(self,cityride,seats):
        print("Type is CityRide")
        super().__init__(cityride,seats=4)

class OffRoad(Car):
    def __init__(self,offroading):
        print(offroading,"Type is Off Roader")
        super().__init__(offroading,seats=6)

class SUV(CityRide,OffRoad):
    def __init__(self):
        print("Vehicle is a SUV")
        super().__init__('RangeRover')

class Bus(Vehicle):
    def __init__(self):
        super().__init__("Bus",seats=50)
    
    def fare(self):
        base=super().fare()
        maintenance=0.10* base
        total=base+maintenance
        return total

instance = Car("sedan")
FinalFare=instance.fare()

print("Final Fare for",instance.vehicle,"is",FinalFare )

