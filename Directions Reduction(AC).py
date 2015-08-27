def dirReduc(arr):
    a = arr
    c = {}
    c['NORTH'] = 'SOUTH'
    c['SOUTH'] = 'NORTH'
    c['EAST'] = 'WEST'
    c['WEST'] = 'EAST'
    while True:
        b = []
        n = len(a)
        i = 0
        while i < n - 1:
            if c[a[i]] == a[i + 1]:
                i += 2
            else:
                b.append(a[i])
                i += 1
        if i < n:
            b.append(a[i])
            i += 1
        if len(a) == len(b):
            a = b
            break
        a = b
    return a
    