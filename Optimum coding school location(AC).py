import sys

def optimum_location(students, locations):
    a = locations
    b = students
    na = len(a)
    nb = len(b)
    mdist = sys.maxint
    mid = mx = my = -1
    for i in xrange(na):
        dist = 0
        id = a[i]['id']
        x = a[i]['x']
        y = a[i]['y']
        for j in xrange(nb):
            dist += abs(b[j][0] - x) + abs(b[j][1] - y)
        if dist < mdist:
            mdist = dist
            mid = id
            mx = x
            my = y
    return 'The best location is number %d with the coordinates x = %d and y = %d' % (mid, mx, my)
    