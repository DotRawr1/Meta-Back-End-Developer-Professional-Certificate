# simple inheritance
# child < parent

# multiple inheritance
# child < parent 1
# child < parent 2

# multi level inheritance
# child 2 < child 1 < parent

# hierarchical inheritance
# child 1 < parent
# child 2 < parent

# hybrid inheritance
# child 1 < parent
# child 2 < parent
# child 3 < child 1
# child 3 < child 2

# inheritance goes bottom to top, left to right when imagining a tree
# called MRO, method resolution order

"""
Y   X
|___|
  |
  Z

Z>Y>X
"""

# pre python 3 - Depth-first search algorithm (DFS)

# python 3 onward - C3 linearization algorithm
# adheres to monotonicity
# follows inheritance graph
# visits super class after local class

class A:
    def d(self):
        return "Function inside A"

class B:
    def d(self):
        return "Function inside B"


class C:
    def d(self):
        return "Function inside C"


class D(A, B):
    def d(self):
        return "Function inside D"


class E(B, C):
    def d(self):
        return "Function inside E"


class F(E,D,C):
    pass

f = F()
print(f.d())
print(F.mro())
print(help(F))
