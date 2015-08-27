def multvec(m, v):
    return [
        m[0][0] * v[0] + m[0][1] * v[1],
        m[1][0] * v[0] + m[1][1] * v[1],
    ]
    
def matmult(a, b):
    c = [[0, 0], [0, 0]]
    for i in xrange(2):
        for j in xrange(2):
            for k in xrange(2):
                c[i][j] += a[i][k] * b[k][j]
    return c
    
def matpow(m, n):
    if n == 1:
        return m
    mp = matpow(m, n >> 1)
    res = matmult(mp, mp)
    if n & 1:
        res = matmult(res, m)
    return res
    
def calcTerm(v, m, n):
    mp = matpow(m, n - 1)
    return multvec(mp, v)[1]
    
def fib(n):
    if n >= 0 and n <= 1:
        return n
    if n > 1:
        return calcTerm([0, 1], [[0, 1], [1, 1]], n)
    else:
        return calcTerm([1, 0], [[0, 1], [1, -1]], 1 - n)
        