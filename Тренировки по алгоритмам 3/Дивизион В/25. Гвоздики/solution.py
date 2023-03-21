def f(c: list) -> int:
    if len(c) == 2:
        return c[1] - c[0]
    dp = [0] * len(c)
    dp[1] = c[1] - c[0]
    dp[2] = c[2] - c[1] + dp[1]
    for i in range(3, len(c)):
        dp[i] = min(dp[i-2], dp[i-1]) + c[i] - c[i-1]
    return dp[-1]


input()
print(str(f(sorted(list(map(int, input().split()))))))
