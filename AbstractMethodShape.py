from abc import ABC, abstractmethod
import math
PI=math.pi

class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def get_area(self):
        return PI*self.radius*self.radius
class Rectangle(Shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def get_area(self):
        return self.width*self.height
    
c=Circle(2)
print(c.get_area())
r=Rectangle(3,4)
print(r.get_area())


