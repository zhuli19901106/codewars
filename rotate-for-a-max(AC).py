def max_rot(n):
    s = str(n)
    ls = len(s)
    ret = n
    for i in range(ls):
        s = rotate(s, i, ls)
        ret = max(ret, int(s))
    return ret

def reverse(s, start, end):
    ls = len(s)
    start = max(start, 0)
    end = min(end, ls)
    return s[:start] + s[start:end][::-1] + s[end:]

def rotate(s, start, end):
    s = reverse(s, start, start + 1)
    s = reverse(s, start + 1, end)
    s = reverse(s, start, end)
    return s
