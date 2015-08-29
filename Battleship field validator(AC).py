n = m = 0
corner = [[-1, -1], [-1, +1], [+1, -1], [+1, +1]]
side = [[+1, 0], [0, +1], [-1, 0], [0, -1]]

def inbound(x, y):
    return x >= 0 and x <= n - 1 and y >= 0 and y <= m - 1
    
def validateBattlefield(a):
    global n, m, side, corner
    
    n = len(a)
    m = len(a[0])
    for i in xrange(n):
        for j in xrange(m):
            if not a[i][j]:
                continue
            for k in xrange(4):
                x = i + corner[k][0]
                y = j + corner[k][1]
                if inbound(x, y) and a[x][y]:
                    # Adjacency at four corners detected
                    return False
    c = [0, 0, 0, 0]
    for i in xrange(n):
        for j in xrange(m):
            if not a[i][j]:
                continue
            mll = 0
            for k in xrange(2):
                a[i][j] = 1
                x = i
                y = j
                ll = 0
                while inbound(x, y) and a[x][y]:
                    a[x][y] = 0
                    ll += 1
                    x += side[k][0]
                    y += side[k][1]
                mll = max(mll, ll)
            a[i][j] = 0
            c[mll - 1] += 1
    return c == [4, 3, 2, 1]
    