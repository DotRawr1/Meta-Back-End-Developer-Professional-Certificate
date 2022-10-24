# open(<FILE_NAME> <FILE_LOCATION>, <MODE>)
# mode = action required. read/write/create
# Mode = "r" // open and read text
# Mode = "rb" // open and read binary
# Mode = "r+" // open and read and write
# Mode = "w" // open and write, will overwrite existing file
# Mode = "a" // open for editing and appending

# close() // no arguments
# with open("testing.txt", "r") as file: // no close function needed, automatic

# output = text/binary // text is human friendly, binary is not
# text is default format
# open(<FILE_NAME>, wb) // opens a file in binary for writing


file = open("week-2/errorExceptionFiles/test.txt", mode = "r")
data = file.readline()
# file.readlines() // reads multiple lines in an array
print(data)
file.close()

with open("week-2/errorExceptionFiles/test.txt", mode = "r") as file:
    data = file.readline()
    print(data) # same as above, but more error tolerant and smaller code