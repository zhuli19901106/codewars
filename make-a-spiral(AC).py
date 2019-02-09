d = [[0, +1], [+1, 0], [0, -1], [-1, 0]]

def inbound(x, y, n):
    return x >= 0 and x <= n - 1 and y >= 0 and y <= n - 1
    
def count_neighor(a, x, y):
    n = len(a)
    cc = 0
    for i in xrange(4):
        x1 = x + d[i][0]
        y1 = y + d[i][1]
        if not inbound(x1, y1, n):
            continue
        if a[x1][y1]:
            cc += 1
    return cc
    
def spiralize(n):
    if n <= 0:
        return []
    a = [[0 for j in xrange(n)] for i in xrange(n)]
    x = y = 0
    dir = 0
    while True:
        a[x][y] = 1
        i = 0
        while i < 4:
            x1 = x + d[dir][0]
            y1 = y + d[dir][1]
            if inbound(x1, y1, n) and a[x1][y1] == 0 and count_neighor(a, x1, y1) <= 1:
                x, y = x1, y1
                break
            i += 1
            dir = (dir + 1) % 4
        if i >= 4:
            break
    return a
    