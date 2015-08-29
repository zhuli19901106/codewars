import math

n = 9
nb = int(math.sqrt(n))
n2 = n * n
blank = 0
row = 0
col = 0
block = 0
solved = False

def get2dmatrix(n, m, val):
    return [[val for j in xrange(m)] for i in xrange(n)]

def dfs(a, idx):   
    global solved, blank, row, col, block, n, nb, n2
    
    if solved:
        return
    if idx == len(blank):
        solved = True
        return
    
    x = blank[idx] / n
    y = blank[idx] % n
    for i in xrange(n):
        if row[x][i] or col[y][i] or block[x / nb * nb + y / nb][i]:
            continue
        row[x][i] = col[y][i] = block[x / nb * nb + y / nb][i] = True
        a[x][y] = i + 1
        dfs(a, idx + 1)
        if solved:
            return
        a[x][y] = 0
        row[x][i] = col[y][i] = block[x / nb * nb + y / nb][i] = False

def sudoku(a):
    global solved, blank, row, col, block, n, nb, n2
    
    blank = []
    row = get2dmatrix(n, n, False)
    col = get2dmatrix(n, n, False)
    block = get2dmatrix(n, n, False)
    
    for i in xrange(n2):
        x = i / n
        y = i % n
        val = a[x][y]
        if val > 0:
            row[x][val - 1] = True
            col[y][val - 1] = True
            block[x / nb * nb + y / nb][val - 1] = True
        else:
            blank.append(i)
    solved = False
    dfs(a, 0)
    
    return a