#string defs project
def revers(str):
    # Accept an input string, str, and reverse its characters in order
    "REPLACE THIS CODE WITH YOUR CONVERSION METHOD"
    new = ''
    for i in range (0 , len(str)):
        new += str[len(str) -1 - i]
    return new


def uppercase(str):
    # Convert all the characters of the input string, str, to upper
    # case. Reurn the uppercased string.
    "REPLACE THIS CODE WITH YOUR CONVERSION METHOD"
    return str.upper()

def palindrome(str):
    # Check if the input string, str, is spelled the same forwards
    # as it is spelled backwards.
    # Return "is a palindrome" if it is, or "is not a palindrome" if it is not.
    "REPLACE THIS CODE WITH YOUR CONVERSION METHOD"
    flag = 0
    for i in range (0, len(str)):
        if str[i] != str[len(str) - 1 -i]:
            flag += 1
    if flag > 0:
        return 'is not a palindrome'
    else:
        return 'is a palindrome'
