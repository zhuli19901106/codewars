def lcs(s1, s2):
    n1 = len(s1)
    n2 = len(s2)
    if n1 == 0 or n2 == 0:
        return ''
    dp = [[0 for j in xrange(n2 + 1)] for i in xrange(n1 + 1)]
    for i in xrange(n1):
        for j in xrange(n2):
            if s1[i] == s2[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
    m = dp[n1][n2]
    mj = n1
    mk = n2
    res = []
    for i in xrange(m, 0, -1):
        found = False
        j = i
        while j <= mj:
            k = i
            while k <= mk:
                if s1[j - 1] == s2[k - 1] and dp[j][k] == i:
                    found = True
                    mj = j - 1
                    mk = k - 1
                    res.append(s1[j - 1])
                    break
                else:
                    k += 1
            if found:
                break
            j += 1
    return ''.join(res[::-1])
    
print lcs('abcdef', 'acf')
print lcs('aef', 'acf')
