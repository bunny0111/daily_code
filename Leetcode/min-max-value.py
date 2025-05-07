'''
Find the minimum and maximum value
arr = [2,3,5,54,4,44,3,45,6,1,1,6]
'''
arr = [2,3,5,54,4,44,3,45,6,1,1,6]
min_value = arr[0]
max_value = arr[0]
for i in arr:
    if i < min_value:
        min_value = i
    if i > max_value:
        max_value = i
        
print(min_value, " is minimum value.")
print(max_value, " is maximum value.")