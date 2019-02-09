def array_change(a):
    n = len(a)
    ret = 0
    for i in range(1, n):
        if a[i] <= a[i - 1]:
            ret += a[i - 1] + 1 - a[i]
            a[i] = a[i - 1] + 1
    return ret
