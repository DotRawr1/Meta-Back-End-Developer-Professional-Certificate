# building blocks for adding functionality
# modules are imported at the beginning, but can be defined at any point

## scope
# modules create seperate namespace
# 2 modules can have functions with the same name
## reusablilty
## simplicity
# modules are built with simple purposes in mind
# avoids interdepentency among modules

# any python file can be a module
# search order:
# current directory > built in module directory > pythonpath > default directory

import sys
locations = sys.path
for i in locations:
    print(i)

import calendar
leapdays = calendar.leapdays(2000, 2050)
print(leapdays) # 13
isitleap = calendar.isleap(2036)
print(isitleap) # true

# sys.path.insert(1, r'C:\Sample\Path\Here')
# imports wont show as recognized by the IDE, but they will work

from math import sqrt
root = sqrt(9)
print(root) 

import math as m
cosine = m.cos(0)
print(cosine)

from math import factorial as f
factorial_10 = f(10)
print(factorial_10)

from math import factorial, log10, sqrt
x = log10(50)
print(x)

# from math import *
# import all from math module
# includes variables