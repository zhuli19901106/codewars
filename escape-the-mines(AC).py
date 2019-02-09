n = m = 0
dname = ['right', 'left', 'down', 'up']
dir = [[+1, 0], [-1, 0], [0, +1], [0, -1]]
suc = 0

def inbound(x, y):
    global n, m
    return x >= 0 and x <= n - 1 and y >= 0 and y <= m - 1
    
def dfs(a, start, end, path):
    global n, m, dname, dir, suc
    
    if start == end:
        suc = True
        return
    x = start / m
    y = start % m
    for i in xrange(4):
        x1 = x + dir[i][0]
        y1 = y + dir[i][1]
        if not (inbound(x1, y1) and a[x1][y1]):
            continue
        a[x][y] = False
        path.append(dname[i])
        dfs(a, x1 * m + y1, end, path)
        if suc:
            return
        path.pop()
        a[x][y] = True

def solve(a, start, end):
    global n, m, suc
    
    aa = []
    for row in a:
        aa.append(row[:])
    n = len(aa)
    m = len(aa[0])
    path = []
    suc = False
    dfs(aa, start['x'] * m + start['y'], end['x'] * m + end['y'], path)
    return path
    