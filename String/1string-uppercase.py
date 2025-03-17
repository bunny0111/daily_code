'''
Convert String to Uppercase
Q. Write a function that converts all characters in a string to uppercase.
Input: "hello"
Output: "HELLO"

Don't use built-in functions

Eg. ascii value of 'a' is 97 and 'A' is 65; that means the capital letter is 32 less than the small letter
'''
def stringUpper(s):
    result = ""
    for char in s:
        if 'a' <= char <= 'z':      # input is lying between these or not
            result += chr(ord(char) - 32)      # ord function will provide the ascii code of that char
        else:
            result += char
    return result

s = "Shubham"
print(stringUpper(s))
