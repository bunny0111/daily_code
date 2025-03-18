'''
Write a python program to reverse a string
'''
def stringReverse(s):
    rev = ""
    for char in s:
        rev = char + rev
    return rev
print(stringReverse("Hello"))