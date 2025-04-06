def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [10, 5, 8, 7, 9]
target = 9
result=linear_search(arr, target)
if result != -1:
    print(f"Result found at index {result}")
else:
    print("Not found")