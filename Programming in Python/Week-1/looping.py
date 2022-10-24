for i in range(10):
    print("Looping..", i)

count = 0
while count < 6:
    print(str(count))
    count += 1

letters = ["a", "b", "c", "d", "e"]
for idx, item in enumerate(letters):
    print(idx, item)


favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Chocolate Cake', 'Beans', 'Tiramisú']
for dessert in favorites:
    if dessert == 'Beans':
        print(dessert, "is not a dessert")
        break # stops
    elif dessert == 'Apple Pie':
        continue # skip then continue
    elif dessert == 'Chocolate Cake':
        pass # ignore
    print('I like', dessert) 
else:
    print('No sorry, not a dessert on my list')