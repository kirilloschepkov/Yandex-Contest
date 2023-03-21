def f(m, n: int) -> int:
    dp = [1] * (m + 1)
    dp[0] = 0
    for _ in range(n - 1):
        current = dp.copy()
        for k in range(1, m + 1):
            dp[k] = 0
            for i in range(k):
                dp[k] += current[i] + current[i + 1]
    return dp[-1]


print(str(f(*map(int, input().split()))))
