def bubble_sort(nums):
    for i in range(len(nums)-1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

arr = [1, 3, 0, 9, 1, 0, 6, 0, 5, 7]
result = bubble_sort(arr)
print(result)