# read() // returns a string that contains all characters
# print(file.read(x)) // only first x characters

# readline() // returns only first line
# print(file.readline(x)) // specificed x characters on first line

# readlines() // returns entire contents in ordered list
# print(file.readlines)

#paths // absolute or relative
# absolute
# user/local/etc/file.txt
# C:\users\system\file.txt
# relative
# somefile.txt
# ./somefile.txt

with open("week-2/errorExceptionFiles/sample.txt", "r") as file:
    # print(file.read()) # entire file as-is
    # print(file.read(44)) // first 44 characters, starting at 0 including 44
    # print(file.readline()) // just the first line
    # print(file.readlines()) // entire text, formatted, in square brackets
    for x in file:
        print(x)



import random
f = open("week-2/errorExceptionFiles/petnames.txt", "r") # declare file
f_content = f.read() # declare var with file data
f_content_list = f_content.split("\n") # splits file into a list
print(random.choice(f_content_list)) # picks a name at random

# alternatively, tp pick a file to open
# import random
# f_name = input('Type the file name: ') // asks for file input
# f = open(f_name) # "r" omitted as it's the default
# f_content = f.read()
# f_content_list = f_content.split("\n")
# print(random.choice(f_content_list))