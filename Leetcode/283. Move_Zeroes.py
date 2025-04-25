'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]
'''
def move_zeros(nums):
    non_zero = 0    # This pointer keeps track of the position to place the next non-zero value
    for i in range(len(nums)):
        if nums[i] != 0:
            # Swap current non-zero with the element at index non_zero
            nums[i], nums[non_zero] = nums[non_zero], nums[i]
            non_zero += 1
    return nums
arr1 = [0,1,0,3,12]
arr2 = [0]
print(move_zeros(arr1))
print(move_zeros(arr2))
