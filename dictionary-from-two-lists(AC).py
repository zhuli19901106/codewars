def createDict(keys, values):
    a = {}
    n = len(keys)
    m = len(values)
    for i in xrange(n):
        a[keys[i]] = values[i] if i < m else None
    return a
    