# Recursion + Memorization
ack = {}

def Ackermann(m, n):
    if (m, n) in ack:
        return ack[(m, n)]
    if m == 0:
        ack[(m, n)] = n + 1
        return ack[(m, n)]
    if n == 0:
        ack[(m, n)] = Ackermann(m - 1, 1)
        return ack[(m, n)]
    ack[(m, n)] = Ackermann(m - 1, Ackermann(m, n - 1))
    return ack[(m, n)]
    