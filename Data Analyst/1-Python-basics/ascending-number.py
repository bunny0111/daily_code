'''
Write a python program to sort a list of numbers in a ascending order
'''
numbers = [int(x) for x in input("Enter numbers separated by space: ").split()]
numbers.sort()
print(f"Sorted list: {numbers}")