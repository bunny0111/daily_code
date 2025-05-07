def linear_search(nums, n):
    for i in range(len(nums)):
        if nums[i] == n:
            return i
    return -1
arr = [10, 5, 8, 4, 6, 9, 2]
n = 8
print(linear_search(arr, n))