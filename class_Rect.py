class Rect:
    def __init__(self,height,width):
        self.height=height
        self.width=width

    def calArea(self):
        return self.height*self.width
    
rectangle=Rect(5,6)

area=rectangle.calArea()
print(area)