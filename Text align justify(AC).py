import re

def justify(text, width):
    a = re.split('\s+', text)
    n = len(a)
    i = 0
    ans = []
    while i < n:
        ll = 0
        j = i
        while j < n:
            ll += len(a[j])
            if ll + (j - i) > width:
                ll -= len(a[j])
                break
            j += 1
        if j == i:
            j = i + 1
        if j == i + 1:
            ans.append(a[i])
            i = j
            continue
        cc = j - i - 1
        line = []
        line.append(a[i])
        if j == n:
            ans.append(' '.join(a[i: j]))
            break
        for k in xrange(cc):
            line.append(' ' * ((width - ll) / cc + 1) if k < (width - ll) % cc else ' ' * ((width - ll) / cc))
            line.append(a[i + k + 1])
        ans.append(''.join(line))
        i = j
    return '\n'.join(ans)
    