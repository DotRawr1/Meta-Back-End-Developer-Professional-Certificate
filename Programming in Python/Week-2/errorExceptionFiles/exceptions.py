# syntax errors = human errors ie. typos, misspellings
# exceptions = logic errors, ie. dividing 5 by zero

def divideBy(a,b):
    return a / b
try:
    ans = divideBy(40,0)
except ZeroDivisionError as e:
    print(e, "we cannot divide by zero")
except Exception as e:
    print(e, "something went wrong")


items = [1,2,3,4,5]
try:
    item = items[6]
    print(item)
except:
    print("Item does not belong in the list")


def divide_by(a, b):
    return a / b
try:
    ans = divide_by(40, 0)
    print(ans)
except ZeroDivisionError:
    print(0)
except Exception as e:
    print(e, "Something went wrong!")


try:
    with open('file_does_not_exist.txt', 'r') as file:
        print(file.read())
except:
    print("The file could not be found")