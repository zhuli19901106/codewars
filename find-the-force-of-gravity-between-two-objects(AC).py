def solution(a, b):
    m1 = norm_mass(a[0], b[0])
    m2 = norm_mass(a[1], b[1])
    d = norm_dist(a[2], b[2])
    G = 6.67e-11
    return G * m1 * m2 / (d ** 2)

def norm_mass(val, unit):
    m = {'kg': 1, 'g': 1e-3, 'mg': 1e-6, 'μg': 1e-9, 'lb':  0.453592}
    return val * m[unit]

def norm_dist(val, unit):
    m = {'m': 1, 'cm': 1e-2, 'mm': 1e-3, 'μm': 1e-6, 'ft': 0.3048}
    return val * m[unit]
