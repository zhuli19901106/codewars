import math

def countPerm(c):
    res = 1
    res *= math.factorial(sum(c.values()))
    for val in c.values():
        res /= math.factorial(val)
    return res
    
def listPosition(word):
    w = map(ord, list(word))
    n = len(w)
    
    res = 0
    i = 0
    while i < n:
        h = sorted(list(set(w[i:])))
        hl = len(h)
        c = dict.fromkeys(h, 0)
        
        for ch in w[i:]:
            c[ch] += 1
        
        for j in xrange(hl):
            if h[j] == w[i]:
                break
            c[h[j]] -= 1
            res += countPerm(c)
            c[h[j]] += 1
        i += 1
    return res + 1
    