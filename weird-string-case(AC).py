import re

def fun(s):
    n = len(s)
    s = list(s)
    for i in xrange(n):
        if i & 1:
            s[i] = s[i].lower()
        else:
            s[i] = s[i].upper()
    return ''.join(s)
    
def to_weird_case(string):
    return ' '.join(map(fun, re.split('\s+', string)))
    