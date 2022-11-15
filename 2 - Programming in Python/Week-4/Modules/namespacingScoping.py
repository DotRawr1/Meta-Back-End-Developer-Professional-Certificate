# Local > Enclosed > Global > Built-in
# scope resolution follows the LEGB rule
# local - inside function. global - outside function

def d():
    animal = "elephant"
    def e():
        nonlocal animal
        animal = "giraffe"
        print("Inside nested function: " + animal)
    print("Before calling function: " + animal)
    e()
    print("After nested function: " + animal)

animal = "camel"
d()
print("Global animal: " + animal)