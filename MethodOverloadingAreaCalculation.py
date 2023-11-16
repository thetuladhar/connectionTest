class ShapeCalculator:
    def area(self, *args):
        if len(args) == 1:
            return args[0] ** 2  
        elif len(args) == 2:
            return args[0] * args[1]  
            raise ValueError("Invalid number of arguments")

calculator = ShapeCalculator()


#One Parameter
square = calculator.area(5)
print(square)

#Two Parameters
rectangle_area = calculator.area(4, 6)
print(rectangle_area)