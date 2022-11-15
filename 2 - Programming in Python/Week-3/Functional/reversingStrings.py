# str[start:stop:step]
# extended slice syntax
trial = "reversal"
new_trail = trial[::-1]
print(new_trail)

# recursion
def reverseString(str):
    if len(str) == 0:
        return str
    else:
        return reverseString(str[1:]) + str[0]
print(reverseString("reversal"))