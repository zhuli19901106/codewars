suc = 0

def dfs(s, n, a):
    global suc
    
    if s == 0 and len(a) > 2:
        a.pop()
        suc = True
        return
    s -= n * n
    i = n - 1
    while i * (i + 1) * (2 * i + 1) / 6 >= s:
        if i * i > s:
            i -= 1
            continue
        a.append(i)
        dfs(s, i, a)
        if suc:
            return
        a.pop()
        i -= 1
    s += n * n
    
def decompose(n):
    global suc
    
    suc = False
    a = []
    i = n - 1
    while i * (i + 1) * (2 * i + 1) / 6 >= n * n:
        a.append(i)
        dfs(n * n, i, a)
        if suc:
            break
        a.pop()
        i -= 1
    return a[::-1] if len(a) > 1 else None
    