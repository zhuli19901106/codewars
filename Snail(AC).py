# This problem is bugged.
# The test data is not clearly specified in the problem description.
'''
import sys

def inbound(x, y, n):
    return x >= 0 and x <= n - 1 and y >= 0 and y <= n - 1
    
def snail(array):
    d = [[0, +1], [+1, 0], [0, -1], [-1, 0]]
    a = array
    n = len(a)
    b = [[False for j in xrange(n)] for i in xrange(n)]
    cc = n * n
    dir = 0
    
    x = y = 0
    res = []
    while cc > 0:
        res.append(a[x][y])
        b[x][y] = True
        cc -= 1
        for i in xrange(4):
            x1 = x + d[dir][0]
            y1 = y + d[dir][1]
            if (not b[x1][y1]) and inbound(x1, y1, n):
                x = x1
                y = y1
                break
            dir = (dir + 1) % 4
    return res
'''
# This is the most rated solution
def snail(array):
    return list(array[0]) + snail(zip(*array[1:])[::-1]) if array else []
    