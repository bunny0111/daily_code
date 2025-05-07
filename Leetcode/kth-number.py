def find_kth_number(arr, k):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr[k - 1]

arr = [7, 10, 4, 3, 20, 15]
k = 3
print(find_kth_number(arr, k))