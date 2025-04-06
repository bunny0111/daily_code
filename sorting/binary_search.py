def binary_search(arr, n):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left+right)//2

        if arr[mid] == n:
            return mid
        elif arr[mid] < n:
            left = mid+1
        else:
            right = mid-1
    return -1

arr = [1, 3, 5, 7, 9, 11]
n = 9
result = binary_search(arr, n)
if result != -1:
    print(f"Element found at {result}")
else:
    print("Not found")