set1 = {1, 2, 3, 4, 5, 5}

print(set1) # does not handle doubles, wont print 2 5s
set1.add(6)
print(set1)
set1.remove(2)
set1.discard(5) # both remove specified
print(set1)

print("/ / / / / / / / / / / / / / / / /f")

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print(set_a.union(set_b)) # merges, minus the dupliucates
# print( set_a | set_b)

print(set_a.intersection(set_b)) # shared
# print(set_a & set_b)

print(set_a.difference(set_b)) # a excluding b duplicates
# print(set_a - set_b)

print(set_a.symmetric_difference(set_b)) # a + b excluding duplicates
# print(set_a ^set_b)

print("/ / / / / / / / / / / / / / /")

# set1.remove[0] // TypeError, not scriptable