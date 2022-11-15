# palindromes
"""
def isPalindrome(str):
    startIndex = 0
    endIndex = len(str) - 1
    for x in str:
        if str[startIndex] != str[endIndex]:
            return False
    return True
print(isPalindrome("racecar")) """

def isPalindrome(str):
    startIndex = 0
    endIndex = len(str) - 1
    for x in str:
        if str[startIndex] != str[endIndex]:
            return False
    newString = ""
    reverseString = ""
    for letter in str:
        if letter != " ":
            newString = newString + letter
            reverseString = letter + reverseString
        if newString.lower() == reverseString.lower():
            return True
    return False

print(isPalindrome("racecar"))
print(isPalindrome("beans"))
print(isPalindrome("murder for a jar of red rum"))