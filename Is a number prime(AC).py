def is_prime(num):
    n = num
    if n < 2:
        return False
    i = 2
    while i <= n / i:
        if n % i == 0:
            return False
        i += 1
    return True
    