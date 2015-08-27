def productFib(prod):
    f1 = 0
    f2 = 1
    while f1 * f2 < prod:
        f1, f2 = f2, f1 + f2
    return [f1, f2, prod == f1 * f2]
    