# What is Instantiation in terms of OOP terminology

# when we create object for a class is called instantiation in object oriented programming

class A:
    def get(self, a):
        self.a =a 
    def put(self):
        print("A : ", self.a)

a1 = A() # this is called instantiation
a1.get(10)
a1.put()