def mineLocation(field):
    n = len(field)
    m = len(field[0])
    for i in xrange(n):
        for j in xrange(m):
            if field[i][j]:
                return [i, j]
                