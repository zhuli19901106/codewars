def solution(n):
    u = ['I', 'V', 'X', 'L', 'C', 'D', 'M', ]
    w = [1, 5, 10, 50, 100, 500, 1000]
    i = 0
    m = {}
    i = 0
    while i + 2 < len(u):
        for j in xrange(3):
            m[(j + 1) * w[i]] = (j + 1) * u[i]
        m[4 * w[i]] = u[i] + u[i + 1]
        for j in xrange(4):
            m[(j + 5) * w[i]] = u[i + 1] + (j * u[i])
        m[9 * w[i]] = u[i] + u[i + 2]
        i += 2
    for j in xrange(3):
            m[(j + 1) * w[i]] = (j + 1) * u[i]
    val = 1000
    ans = ''
    while val > 0:
        if n < val:
            val /= 10
            continue
        ans += m[n / val * val]
        n %= val
        val /= 10
    return ans
    