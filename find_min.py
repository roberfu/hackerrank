def find_min(arr):
    if len(arr) == 0:
        return -1
    if len(arr) == 1:
        return arr[0]
    n = arr.pop()
    if (n < arr[0]):
        arr[0] = n
    return find_min(arr)

print(find_min([6,2,2,3,4,1,5])) # 1