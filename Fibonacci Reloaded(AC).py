def fib(n):
    f1 = 0
    f2 = 1
    if n < 1:
        return 1.0
    if n < 3:
        return n - 1
    for i in xrange(n - 2):
        f3 = f1 + f2
        f1 = f2
        f2 = f3
    return float(f3)
    