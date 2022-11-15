menu = ["espresso", "mocha", "latte", "cappuccino", "cortado", "americano"]

def findCoffee(coffee):
    if coffee[0] == "c":
        return coffee

# map takes all objects in a list and applies a function
mapCoffee = map(findCoffee, menu)
print(mapCoffee)
for x in mapCoffee:
    print(x)

# filters do the same, but they make a new list with only true values
filterCoffee = filter(findCoffee, menu)
print(filterCoffee)
for x in filterCoffee:
    print(x)