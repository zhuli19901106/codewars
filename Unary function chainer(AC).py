'''
# I didn't know it could be so simple...
def comp2(f1, f2):
    return lambda x: f1(f2(x))
    
def chained(functions):
    f = []
    f.append(functions[0])
    n = len(functions)
    for i in xrange(1, n):
        f.append(comp2(functions[i], f[-1]))
    return f[-1]
'''
def chained(functions):
    def f(x):
        for function in functions:
            x = function(x)
        return x
    return f
    