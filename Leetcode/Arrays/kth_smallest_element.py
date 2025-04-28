'''
Find the kth smallest element in an array in linear time complexity
'''
# Method 1
print("Method-1")
def kth_smallest_element(arr, k):
    arr.sort()
    return arr[k - 1]
arr = [7, 10, 4, 3, 20, 15]
k = 3
print(kth_smallest_element(arr, k))

# Method 2
print("Method-2")
import heapq
def kth_smallest_element(arr, k):
    heapq.heapify(arr)
    for _ in range(k-1):
        heapq.heappop(arr)
    return heapq.heappop(arr)
arr = [7, 10, 4, 3, 20, 15]
k = 4
print(kth_smallest_element(arr, k))

# Method 3
print("Method-3")
def kth_smallest_element(arr, k):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                arr[j], arr[min_index] = arr[min_index], arr[j]
    return arr[k-1]
arr = [7, 10, 4, 3, 20, 15]
k = 2
print(kth_smallest_element(arr, k))
'''if arr[j] < arr[min_index]: --> If arr[j] is smaller than arr[min_index], it means: - We found a new smaller element. So, we should update min_index to j.'''