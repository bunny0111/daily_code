'''
Given an array consisting of only 0s, 1s and 2s. Write a program to in-place sort the array without using inbuilt sort functions, in linear time complexity and constant space.

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
'''
def sort_color(nums):
    count0 = count1 = count2 = 0
    for num in nums:
        if num == 0:
            count0 += 1
        elif num == 1:
            count1 += 1
        else:
            count2 += 1

    for i in range(len(nums)):
        if i < count0:
            nums[i] = 0
        elif i < count0 + count1:
            nums[i] = 1
        else:
            nums[i] = 2

nums = [2,0,2,1,1,0]
sort_color(nums)
print(nums)