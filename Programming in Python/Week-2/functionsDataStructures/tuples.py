tuple1 = (1, "string", 4.5, True)
print(type(tuple1)) # tuple
print(tuple1.count("string")) # 1
print(tuple1.index(4.5)) # 2
for x in tuple1: # prints all values
    print(x)
# tuple1[0] = 5 // cannot change tuple - immutable