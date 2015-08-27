def is_prime(n):
    'Return True if n is a prime number otherwise return False'
    if n < 2:
        return False
    i = 2
    while i <= n / i:
        if n % i == 0:
            return False
        i += 1
    return True
    