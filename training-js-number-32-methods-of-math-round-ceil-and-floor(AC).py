import math

def round_it(n):
    s = str(n)
    pos = s.find('.')
    l1 = pos
    l2 = len(s) - pos - 1
    if l1 < l2:
        return math.ceil(n)
    elif l1 > l2:
        return math.floor(n)
    else:
        return round(n)
