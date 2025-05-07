def missing_number(nums):
    n = len(nums) + 1
    expected_sums = n * (n+1)//2
    actual_sum = sum(nums)
    return expected_sums - actual_sum

nums = [1, 2, 3, 6, 4, 8, 7]
print(missing_number(nums))