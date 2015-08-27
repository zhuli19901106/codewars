def presses(phrase):
    a = {}
    c = [3, 3, 3, 3, 3, 4, 3, 4]
    j = 0
    for k in xrange(len(c)):
        for i in xrange(c[k]):
            a[chr(ord('A') + j)] = i + 1
            a[chr(ord('a') + j)] = i + 1
            j += 1
        a[chr(ord('0') + (k + 2) % 10)] = c[k] + 1
    a[' '] = 1
    a['0'] = 2
    a['1'] = 1
    a['*'] = 1
    a['#'] = 1
    
    return sum(map(a.get, list(phrase)))
    