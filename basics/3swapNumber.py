'''
Write a python program to swap the values of two variables.
'''

def swapNumber(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b
a = 2
b = 3
print(f"{a} and {b} before swap")
print("a and b after swapping",swapNumber(a, b))