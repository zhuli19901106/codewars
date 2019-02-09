# return the sum of the two polynomials p1 and p2.  
def poly_add(p1, p2):
    n1 = len(p1)
    n2 = len(p2)
    if n1 < n2:
        return poly_add(p2, p1)
    ret = []
    for i in range(n2):
        ret.append(p1[i] + p2[i])
    for i in range(n2, n1):
        ret.append(p1[i])
    return ret
