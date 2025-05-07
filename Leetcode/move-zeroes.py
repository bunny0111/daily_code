def move_zeroes(nums):
    non_zero = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[non_zero] = nums[non_zero], nums[i]
            non_zero += 1
    return nums
arr = [1, 0, 6, 0, 8, 9, 4]
print(move_zeroes(arr))