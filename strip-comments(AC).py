# This problem contains Unicode test cases.
import re

ENCODING = 'utf8'

def solution(s, m):
    m = ''.join(m)
    a = re.split('\n', s.decode(ENCODING))
    n = len(a)
    m = set(list(m.decode(ENCODING)))
    for i in xrange(n):
        ll = len(a[i])
        for j in xrange(ll):
            if not a[i][j] in m:
                continue
            a[i] = a[i][:j]
            break
        a[i] = a[i].rstrip()
    return ('\n'.join(a)).encode(ENCODING)
    