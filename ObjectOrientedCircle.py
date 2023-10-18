import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def calculate_circumference(self):
        return 2 * math.pi * self.radius

    def display_properties(self):
        print(f"Circle Radius: {self.radius}")
        print(f"Circle Area: {self.calculate_area()}")
        print(f"Circle Circumference: {self.calculate_circumference()}")

# Get the radius from the user
radius = float(input("Enter the radius of the circle: "))

# Create a Circle object
my_circle = Circle(radius)

# Display the circle properties
my_circle.display_properties()