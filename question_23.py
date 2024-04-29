# Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle

class Rectangle:
    def __init__(self, length, width):
        self.l = length
        self.w = width

    def area(self):
        return self.l*self.w

a1 = Rectangle(10,5)
print("Area of rectangle is : ", a1.area())
