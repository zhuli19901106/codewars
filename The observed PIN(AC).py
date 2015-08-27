'''
# My solution is way too C++, clumsy.
def dfs(observed, code, i, ans, n, m):
    if i == n:
        ans.append(''.join(code))
        return
    for val in m[observed[i]]:
        code.append(val)
        dfs(observed, code, i + 1, ans, n, m)
        code.pop()

def get_pins(observed):
    m = {}
    m['1'] = '124'
    m['2'] = '1235'
    m['3'] = '236'
    m['4'] = '1457'
    m['5'] = '24568'
    m['6'] = '3569'
    m['7'] = '478'
    m['8'] = '57890'
    m['9'] = '689'
    m['0'] = '80'
    
    ans = []
    n = len(observed)
    dfs(observed, [], 0, ans, n, m)
    return ans
'''
from itertools import product

def get_pins(observed):
    a = ['80', '124', '1235', '236', '1457', '24568', '3569', '478', '57890', '689']
    return [''.join(j) for j in product(*(a[int(i)] for i in observed))]
    