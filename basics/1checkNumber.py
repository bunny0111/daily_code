'''
Write a Python program to check if a number is positive, negative, or zero.
'''
def checkNumbers(n):
    if n == 0:
        return "Zero"
    elif n > 0:
        return "Positive"
    else:
        return "Negative"
    
print(checkNumbers(0))
print(checkNumbers(10))
print(checkNumbers(-20))
