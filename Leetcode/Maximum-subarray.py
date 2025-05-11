'''
Given an integer array arr, find the contiguous subarray
(containing at least one number) which has the largest sum
and return its sum and print the subarray.

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
'''

def maximum_subarray(nums):
    max_sum = current_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum
nums = [5,4,-1,7,8]
print(maximum_subarray(nums))