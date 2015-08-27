def collatz(n):
    a = []
    while True:
        a.append(str(n))
        if n == 1:
            break
        n = n * 3 + 1 if n & 1 else n >> 1
    return '->'.join(a)
    