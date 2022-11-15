# a function that calls itself
# advantages: neat code, broken into sub problems, easier to understand sequences
# disadvantages: hard to follow, memory intensive, hard to debug
# looping solution
def find_factorial_looping(n):
    if n<0:
        return 0
    else:
        factorial = 1
        for i in range(1,n+1):
            factorial=factorial*i
        return factorial

# recursive solution
def find_factorial_recursive(n):
    if n == 1:
        return n
    else:
        return n * find_factorial_recursive(n-1)

print(find_factorial_looping(5))
print(find_factorial_recursive(5))
# = 5 * factorial(4)
# = 5 * (4 * factorial(3))
# = 5 * (4 * (3 * factorial(2)))
# = 5 * (4 * (3 * (2 * factorial(1))))
# = 5 * (4 * (3 * (2 * (factorial(1)))))
# = 5 * (4 * (3 * (2 * (1 * 1)))
# = 5 * (4 * (3 * (2 * 1)))
# = 5 * (4 * (3 * 2))
# = 5 * (4 * 6)
# = 5 * 25
# = 120