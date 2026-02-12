def sum_list(ar):
    if len(ar) == 1:
        return ar[0]
    n = ar.pop()
    return n + sum_list(ar)

print(sum_list([1, 2, 3, 4])) # 10