def count_digits(n):
    if n <= 9:
        return 1
    return 1 + count_digits(n // 10)

print(count_digits(12345)) # 5