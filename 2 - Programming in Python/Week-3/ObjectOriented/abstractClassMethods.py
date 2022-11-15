# abstract classes
# cannot create instance
# need to import a module
# need to be defined before implementation
# abstract class can have one or more abstract methods
# child of abstract class can only be instantiated if abstract methods are overridden

from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def donate(self):
        pass
class Donation(Employee):
    def donate(self):
        a = input("How much would you like to donate?")

amounts = []
john = Donation()
j = john.donate()
amounts.append(j)
peter = Donation()
p = peter.donate()
amounts.append(p)

print(amounts)