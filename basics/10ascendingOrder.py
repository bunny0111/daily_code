'''
Write a python program to sort a list of number in ascending order
'''

def ascending_order(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = ascending_order(numbers)
print("Sorted list:", sorted_numbers)