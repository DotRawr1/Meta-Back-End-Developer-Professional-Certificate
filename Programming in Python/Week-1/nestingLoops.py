list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
count = 0
for x in list1:
    count += 1
    for y in list2:
        count += 1
print(count) # 90

for i in range(5):
    for j in range(5):
        print(0, end=" ")
    print()