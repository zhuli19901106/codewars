def isValidWalk(walk):
    d = {
        's': [0, -1],
        'n': [0, +1],
        'w': [-1, 0],
        'e': [+1, 0],
    }
    x, y = 0, 0
    if len(walk) != 10:
        return False
    for w in walk:
        x += d[w][0]
        y += d[w][1]
    return x == 0 and y == 0
    