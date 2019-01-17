class Rectangle:
    def __init__(self, height, width):
        self.height=height
        self.width=width

rect1 = Rectangle(20,60)
rect2 = Rectangle(50,40)


print ("area is:", rect1.height* rect1.width)
print ("area is:", rect2.height*rect2.width)