import math

def m2d(n, m, val):
    return [[val for j in xrange(m)] for i in xrange(n)]
    
class Sudoku(object):
    n = 0
    nb = 0
    grid = row = col = block = 0
    
    def __init__(self, gr):
        self.n = len(gr)
        n = self.n
        
        self.nb = int(math.sqrt(self.n))
        self.row = m2d(n, n, False)
        self.col = m2d(n, n, False)
        self.block = m2d(n, n, False)
        self.grid = []
        
        nb = self.nb
        r = self.row
        c = self.col
        b = self.block
        g = self.grid
        for i in xrange(n):
            g.append(gr[i][:])
            
    def is_valid(self):
        n = self.n
        nb = self.nb
        r = self.row
        c = self.col
        b = self.block
        g = self.grid
        for i in xrange(n):
            for j in xrange(n):
                if type(g[i][j]) != int or not g[i][j] or g[i][j] > n:
                    return False
                if r[i][g[i][j] - 1]:
                    return False
                r[i][g[i][j] - 1] = True
                if c[j][g[i][j] - 1]:
                    return False
                c[j][g[i][j] - 1] = True
                if b[i / nb * nb + j / nb][g[i][j] - 1]:
                    return False
                b[i / nb * nb + j / nb][g[i][j] - 1] = True
        return True
        