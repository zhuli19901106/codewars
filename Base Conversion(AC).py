def convert(a, s, t):
    s = list(s)
    t = list(t)
    hs = {}
    ht = {}
    ls = len(s)
    lt = len(t)
    for i in xrange(ls):
        hs[s[i]] = i
    for i in xrange(lt):
        ht[t[i]] = i
    n = 0
    for ch in a:
        n = n * ls + hs[ch]
    res = []
    while n > 0:
        res.append(t[n % lt])
        n /= lt
    if len(res) == 0:
        res.append(t[0])
    return ''.join(res[::-1])
    