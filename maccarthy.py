def maccarthy(n):
    if (n>100):
        return n-10
    return maccarthy(maccarthy(n+11))


print(maccarthy(99)) # 91