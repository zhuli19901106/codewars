def to_bytes(n):
    bt = 8
    s = bin(n)[2:]
    s = ''.join(['0' for i in range((bt - len(s) % bt) % bt)]) + s
    a = [s[i * bt: i * bt + bt] for i in range(len(s) // bt)]
    return a
