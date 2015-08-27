def char_freq(message):
    m = {}
    for ch in message:
        if ch in m:
            m[ch] += 1
        else:
            m[ch] = 1
    return m
    