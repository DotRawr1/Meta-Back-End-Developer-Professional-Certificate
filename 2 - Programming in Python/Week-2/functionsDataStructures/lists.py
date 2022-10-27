list1 = [1,2,3,4,5]
# print(list1[1]) // 2
list2 = ["A", "B", "C"]
# print(list2[1]) // "B"
list3 = ["Hello", 1, True, 40.22]
# print(list3[1]) // 1

list4 = [1, [2,3,4], 5, 6] # nested lists VALID

# print(*list1) // another way to list
print(list1, sep = " ")
# for x in list1: // more listing
#     print("Value: ", x)

list1.insert(len(list1), 7) # same as append
list1.append(8)
print(list1, sep = " ")

list1.extend([9,10,11])
print(list1, sep = " ")

list1.pop(4)
print(list1, sep = " ")

del list1[2]
print(list1, sep = " ")

