class Alpha:
    def __init__(self):
        self.a = 2  # public, access anywhere by anything
        self._b = 2  # protected, access by other members of the class and its subclasses
        self.__c = 2 # private, only access from its own class
class Parent:
    "Members of parent class"
class Child(Parent):
    "Inherited members from parent class"
    "Additional members of the child class"

######################################################

class MyClass:
    a = 5
    def hello(self):
        print("Hello, world!")

myc = MyClass()
print(myc.a)
print(myc.hello())
