# Explain Inheritance in Python with an example? What is init? Or What Is A Constructor In Python?

# inheritance allows you to inherit properties of parent class to child class. there are five types of inheritance. single, multiple, 
# multilevel, hierarichal and hybrid. following is the example single inheritance.

class A:
    def getA(self,a):
        self.a=a
    def putA(self):
        print("A : ", self.a) 
class B(A):
    def getB(self,b):
        self.b=b 
    def putB(self):
        print("B : ",self.b)

b1 = B()
b1.getA(10)
b1.getB(20)
b1.putA()
b1.putB()

# init function is called every time class is being used to create a new object.

