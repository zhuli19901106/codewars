def checkRow(b, r, val):
    for i in xrange(3):
        if b[r][i] != val:
            return False
    return True
    
def checkCol(b, c, val):
    for i in xrange(3):
        if b[i][c] != val:
            return False
    return True
    
def checkDiag(b, val):
    return b[0][0] == val and b[1][1] == val and b[2][2] == val
    
def checkAntidiag(b, val):
    return b[0][2] == val and b[1][1] == val and b[2][0] == val
    
def isSolved(board):
    b = board
    c0 = 0
    for i in xrange(3):
        for j in xrange(3):
            if b[i][j] == 0:
                c0 += 1
    for val in [1, 2]:
        for i in xrange(3):
            if checkRow(b, i, val):
                return int(val)
            if checkCol(b, i, val):
                return int(val)
        if checkDiag(b, val):
            return int(val)
        if checkAntidiag(b, val):
            return int(val)
    return -1 if c0 > 0 else 0
    