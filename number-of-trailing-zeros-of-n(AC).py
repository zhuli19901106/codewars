def zeros(n):
    sum = 0
    while n > 0:
        sum += n / 5
        n /= 5
    return sum
    