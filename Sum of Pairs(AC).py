def sum_pairs(a, s):
    n = len(a)
    m = {}
    for i in xrange(n):
        if s - a[i] in m:
            return [s - a[i], a[i]]
        if not a[i] in m:
            m[a[i]] = i
    return None
    