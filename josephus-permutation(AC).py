def josephus(items, k):
    a = items
    ans = []
    i = 0
    while len(a) > 0:
        j = (i + k - 1) % len(a)
        ans.append(a[j])
        del a[j]
        i = j if j < len(a) else 0
    return ans
    