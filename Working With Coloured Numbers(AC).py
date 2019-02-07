from math import sqrt

def same_col_seq(val, k, col):
    n = int((-1 + sqrt(1 + 8 * val)) / 2.0)
    if n * (n + 1) / 2 <= val:
        n = n + 1
    a = [i * (i + 1) // 2 for i in range(n, n + 3  * k)]
    if col == 'red':
        a = [x for x in a if x % 3 == 1]
        a = a[:k]
    elif col == 'yellow':
        a = []
    else:
        a = [x for x in a if x % 3 == 0]
        a = a[:k]
    return a
