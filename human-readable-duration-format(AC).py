def format_duration(seconds):
    n = seconds
    if n == 0:
        return 'now'
    
    a = ['second', 'minute', 'hour', 'day', 'year']
    b = [1, ]
    c = [60, 60, 24, 365]
    for val in c:
        b.append(val * b[-1])
    a = a[::-1]
    b = b[::-1]
    c = []
    for val in b:
        c.append(n / val)
        n %= val
    ans = []
    for i in xrange(len(c)):
        if c[i] == 0:
            continue
        ans.append(str(c[i]) + ' ' + (a[i] + 's' if c[i] > 1 else a[i]))
    if len(ans) == 1:
        return ans[0]
    return ', '.join(ans[:-1]) + ' and ' + ans[-1]
    