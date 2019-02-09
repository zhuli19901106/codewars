MAX_N = 100000
dp = [False for i in range(MAX_N + 1)]
dp[1] = True
for i in range(2, MAX_N + 1):
    if i % 3 == 0 and dp[i // 3]:
        dp[i] = True
    if i - 5 > 0 and dp[i - 5]:
        dp[i] = True

def number_increasing(n):
    if n < 1 or n > MAX_N:
        return False
    return dp[n]
