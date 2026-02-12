def a_very_big_sum(ar):
    if len(ar)==1:
        return ar[0]
    num = ar.pop()
    return num + a_very_big_sum(ar)

print(a_very_big_sum([4, 5, 6])) # 15