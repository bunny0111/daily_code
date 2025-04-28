'''
write a program to reverse an array
input = [1,2,3,4,5]
output = [5,4,3,2,1]
'''
# Method 1. Using reversed() function
'''def reverse_array(nums):
    return list(reversed(nums))
'''
# Method 2. Using slicing
'''def reverse_array(nums):
    return nums[::-1]
'''

# Method 3. Using 2 pointer
def reverse_array(nums):
    start = 0
    end = len(nums) - 1
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1
    return nums
arr = [1,2,3,4,5]
reverse = reverse_array(arr)
print(f"original array: {arr}")
print(f"Reversed array: {reverse}")