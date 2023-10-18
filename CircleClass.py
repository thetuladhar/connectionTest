import math
PI=math.pi


class Circle:
    #constructor
    def __init__(self,radius):
        self.radius = radius

    def calculate_area(self):
        return PI * self.radius * self.radius
    
    def calculate_perimeter(self):
        return 2* PI * self.radius
    #des
    

# Get the radius from the user
radius = float(input("Enter the radius of the circle: "))

my_circle=Circle(radius)

print("Circle Area is : ", my_circle.calculate_area())
print("Circle circum is : ", my_circle.calculate_perimeter())



