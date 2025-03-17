'''
Write a Python Program to find the largest of three numbers
'''
def findLargest(a, b, c):
    if a > b and a > c:
        return f"{a} is largest."
    elif b > a and b > c:
        return f"{b} is largest."
    else:
        return f"{c} is largest."
    
print(findLargest(7, 8, 9))