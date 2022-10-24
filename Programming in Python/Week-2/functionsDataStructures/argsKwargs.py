# args++++++++++++++++++++++++++++++++++++++++++
def sum_of(a,b):
    return a + b
# print(sumOf(4,5,6)) # error

def sumOf(**kwargs): # any number of arguments
    sum = 0
    for k,v in kwargs.items():
        sum += v
    return round(sum, 2)
print(sumOf(coffee=2.99, cake=4.55, juice=2.99))

# kwargs++++++++++++++++++++++++++++++++++++++++++++
