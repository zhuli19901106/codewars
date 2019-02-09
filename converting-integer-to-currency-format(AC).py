def to_currency(price):
    price = str(price)
    n = len(price)
    res = []
    for i in xrange(n - 1, -1, -1):
        res.append(price[i])
        if (n - i) % 3 == 1 and i > 0:
            res.append(',')
    res = res[::-1]
    return ''.join(res)
    