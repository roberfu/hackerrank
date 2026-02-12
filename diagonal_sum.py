def diagonal_sum(ma):
    num = len(ma)
    left_sum = 0
    right_sum = 0
    
    for i in range(num):
        left_sum += ma[i][i]
        right_sum += ma[i][num-1-i]
    
    return abs(left_sum - right_sum)

print(diagonal_sum([[11, 2, 4], [4, 5, 6], [10, 8, -12]])) # 15