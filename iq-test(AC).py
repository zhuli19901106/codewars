import re

def iq_test(numbers):
    a = map(int, re.split('\s+', numbers))
    n1 = n2 = 0
    p1 = p2 = 0
    n = len(a)
    for i in xrange(n):
        if a[i] & 1:
            n1 += 1
            p1 = i
        else:
            n2 += 1
            p2 = i
    return p1 + 1 if n1 == 1 else p2 + 1
    