# What is used to check whether an object o is an instance of class A?

class A:
    def __init__(self, a):
        self.a = a 
        print("A : ", self.a)

a1 = A(10)
print(isinstance(a1, object))