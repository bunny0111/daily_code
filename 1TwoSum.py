'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
'''

nums = [2,7,11,15]
target = 9

def twosum(nums, target):
    hash_map = {}       # Dictionary
    # Enumerate is a built-in function in python that allows you to keep track of the number of iterations (loops) in a loop. 

    for i, num in enumerate(nums):
        # print("index:", i)
        # print("value:", num)
        if target - num in hash_map:
            return [hash_map[target-num], i]
        hash_map[num] = i   # Store index of the current number
    return []

print(twosum(nums, target))


'''
How It Works:

We iterate through the nums list using enumerate(nums), which gives us both:
i: the current index
num: the current number

Checking for a complement:

target - num is the number we need to find in hash_map to form a pair that sums up to target.
If target - num (i.e. 9-2 = 7; if 7 is already) is already present in hash_map, it means we have found two indices that sum to target.
Returning the indices

hash_map[target - num] gives us the index of the previously stored number.
i is the current index.
So, [hash_map[target - num], i] returns the two indices that sum to the target.

'''