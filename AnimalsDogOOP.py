#Single Inheritance Example
class Animals:
    def __init__(self):
        self.legs=4
        self.domestic=True
        self.tail=True
        self.mammal=True

    def isMammal(self):
        if self.mammal:
            print("is a Mammal")
    def isDomestic(self):
        if self.domestic:
            print("is a Domestic")

class Dogs(Animals):
    def __init__(self):
        super().__init__()


#Multiple Inheritance Example
class Horses(Animals):
    def __init__(self):
        super().__init__()
    #additional behaviour
    def hasTailsnLegs(self):
        if self.tail:
            print("Has Tails and Legs")

Marley=Dogs()
Marley.isMammal()

Spirit=Horses()
Spirit.hasTailsnLegs()