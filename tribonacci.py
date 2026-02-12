def tribonacci(n):
    if (n == 3):
        return 1;
    if (n <= 2):
        return 0;
    return tribonacci(n-3) + tribonacci(n-2) + tribonacci(n-1)

print(tribonacci(7)) # 7