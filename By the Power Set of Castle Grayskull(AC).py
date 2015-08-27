from itertools import chain, combinations

def power(s):
    return chain(*[combinations(s, i) for i in xrange(len(s) + 1)])
    