def gcd(x, y):
    return y if x == 0 else gcd(y % x, x)
    
def nbr_of_laps(x, y):
    g = gcd(x, y)
    return [y / g, x / g]
    