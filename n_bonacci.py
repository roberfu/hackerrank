def n_bonacci(n,k):
    if (k == n):
        return 1
    if (k <= n - 1):
        return 0
    return sum(n_bonacci(n, k - i) for i in range(1, n+1))

print(n_bonacci(2, 5)) # 3