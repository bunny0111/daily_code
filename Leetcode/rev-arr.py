def rev_arr(arr):
    i = 0
    j = len(arr) - 1
    
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    return arr

arr = [7, 10, 4, 3, 20, 15]
print(rev_arr(arr))