def f(limit: int, step: int) -> int:
    dp = [0] * (limit + 1)
    dp[1] = 1
    for i in range(2, limit + 1):
        dp[i] = sum([dp[i-j if i - j > 0 else 0] for j in range(1, step + 1)])
    return dp[limit]


print(f(*map(int, input().split())))
