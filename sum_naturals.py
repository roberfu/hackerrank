def sum_naturals(n):
    if n == 0:
        return 0
    return n + sum_naturals(n-1)

print(sum_naturals(5)) # 15