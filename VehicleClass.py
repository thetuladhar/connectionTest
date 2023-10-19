class Vehicle:
    def __init__(self,vehicle):
        print(vehicle,"is a Type of Vehicle")

class Car(Vehicle):
    def __init__(self,cartype):
        print("Type is Car")
        super().__init__(cartype)

class CityRide(Car):
    def __init__(self,cityride):
        print("Type is CityRide")
        super().__init__(cityride)


class OffRoad(Car):
    def __init__(self,offroading):
        print(offroading,"Type is Off Roader")
        super().__init__(offroading)


class SUV(CityRide,OffRoad):
    def __init__(self):
        print("Vehicle is a SUV")
        super().__init__('RangeRover')



c=OffRoad("LandRover")
SUV()
