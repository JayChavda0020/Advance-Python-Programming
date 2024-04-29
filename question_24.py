# Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle 

class Circle:
    def __init__(self,radius):
        self.r = radius

    def area(self):
        return 3.14*(self.r**2)

    def perimeter(self):
        return 2*3.14*self.r

c1 = Circle(5)
print("perimeter is : ", c1.area())
print("Area is : ", c1.perimeter())