def bowling_score(rolls):
    a = rolls
    n = len(a)
    i = 0
    j = 0
    ans = 0
    while i < n and j < 10:
        if a[i] == 10:
            ans += a[i] + a[i + 1] + a[i + 2]
            i += 1
        elif a[i] + a[i + 1] == 10:
            ans += a[i] + a[i + 1] + a[i + 2]
            i += 2
        else:
            ans += a[i] + a[i + 1]
            i += 2
        j += 1
    return ans
    