def m2d(n, m, val):
    return [[val for j in xrange(m)] for i in xrange(n)]
    
def validSolution(board):
    a = board
    r = m2d(9, 9, False)
    c = m2d(9, 9, False)
    b = m2d(9, 9, False)
    for i in xrange(9):
        for j in xrange(9):
            if r[i][a[i][j] - 1]:
                return False
            r[i][a[i][j] - 1] = True
            if c[j][a[i][j] - 1]:
                return False
            c[j][a[i][j] - 1] = True
            if b[i / 3 * 3 + j / 3][a[i][j] - 1]:
                return False
            b[i / 3 * 3 + j / 3][a[i][j] - 1] = True
    return True
    