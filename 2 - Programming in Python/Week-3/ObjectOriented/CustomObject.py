class Recipe():
    # def __new__(cls: type[Self]) -> Self: 
    # placeholder for passing the class as its first argument
    def __init__(self, dish, items, time) -> None: # no function, but serves as a placeholder for self reference
        self.dish = dish
        self.items = items
        self.time = time
    def contents(self):
        print("The " + str(self.dish) + " has " + str(self.items) + \
            " and takes " + str(self.time) + " min to prepare")

pizza = Recipe("Pizza", ["cheese", "bread", "tomato"], 45)
pasta = Recipe("Pasta", ["penne", "sauce"], 55)

print(pizza.contents())
print(pasta.contents())



# Define class MyFirstClass
class MyFirstClass():
        print("Who wrote this?")
    # Define string variable called index
        index = "Author-Book"
    # Define function hand_list()
        def hand_list(self, philosopher, book, year):
        # variable + “ wrote the book: ” + variable
            print(MyFirstClass.index)
            print(philosopher + " wrote the book: " + book + " in " + year)

# Call function handlist()
whodunnit = MyFirstClass()
whodunnit.hand_list("Sun Tzu", "The Art of War", "500 BC")