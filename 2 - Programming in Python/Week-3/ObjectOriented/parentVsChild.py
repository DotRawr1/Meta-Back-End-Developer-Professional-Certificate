# class Someclass() - implies using built in class

# parent/super/base class
    # attribute a
    # behavior b
# child/sub/derived class
    # also attribute a
    # also behavior b

class P: # parent class
    def __init__(self):
        self.a = 7
class C(P): # empty child class, inherits parent class P
    pass
c = C() # instance of child class, inherits child class C, thus inherits parent class P
print(c.a) # 7, from parent class P



class Employees:
    def __init__(self, name, last):
        self.name = name
        self.last = last
class Supervisors(Employees):
    def __init__(self, name, last, password):
        super().__init__(name, last)
        self.password = password
class Chefs(Employees):
    def leave_request(self, days):
        return "May I take a leave for " + str(days) + " days?"

adrian = Supervisors("Adrian", "A", "apple")
emily = Chefs("Emily", "E")
juno = Chefs("Juno", "J")

print(emily.leave_request(3)) # May I take a leave for 3 days?
print(adrian.password) # apple
print(juno.name) # Juno