my_d = {}
# Key : Value
# faster than lists
# can be changed/updated

dict1 = {1: "Coffee", 2: "Tea", 3: "Juice"}
print(dict1[1])
dict1[2] = "Mint Tea"
print(dict1)
del dict1[3]
print(dict1)

print("/ / / / / / / / / / / / / / / / / / / / / / / / / ")

dict2 = {1:"Test", "Name": "Jim"}
print(dict2[1]) # print certain value
dict2[2] = "Test 2" # add
print(dict2)
dict2[1] = "Not a Test!" # replace
print(dict2)
del dict2[1] # delete
print(dict2)
for x in dict2: # prints key values
    print(x)
for key, value in dict2.items(): # print key with value
    print(str(key) + " : " + value)