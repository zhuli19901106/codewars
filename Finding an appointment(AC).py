def cmp(x, y):
    if x[0] != y[0]:
        return -1 if x[0] < y[0] else 1
    elif x[1] != y[1]:
        return -1 if x[1] < y[1] else 1
    else:
        return 0
        
def parse(t):
    return int(t[:2]) * 60 + int(t[-2:])

def totime(t):
    return '%02d:%02d' % (t / 60, t % 60)
    
def merge_interval(a):
    res = []
    n = len(a)
    i = 0
    while i < n:
        j = i + 1
        while j < n and a[i][1] >= a[j][0]:
            a[i][1] = max(a[i][1], a[j][1])
            j += 1
        res.append(a[i][:])
        i = j
    return res
    
def get_start_time(a, d):
    start = '09:00'
    st = parse(start)
    end = '19:00'
    et = parse(end)
    
    n = len(a)
    if n == 0:
        return start
        
    b = []
    for i in xrange(n):
        for val in a[i]:
            b.append(val[:])
    n = len(b)
    for i in xrange(n):
        for j in xrange(2):
            b[i][j] = parse(b[i][j])
    b.sort(cmp = cmp)
    b = merge_interval(b)
    if b[0][0] - st >= d:
        return start
    n = len(b)
    for i in xrange(1, n):
        if b[i][0] - b[i - 1][1] >= d:
            return totime(b[i - 1][1])
    if et - b[-1][1] >= d:
        return totime(b[-1][1])
    return None
    