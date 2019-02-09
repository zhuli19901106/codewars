def tribonacci(signature, n):
    a = signature
    if n < 3:
        return a[: n]
    for i in xrange(3, n):
        a.append(a[i - 1] + a[i - 2] + a[i - 3])
    return a
    