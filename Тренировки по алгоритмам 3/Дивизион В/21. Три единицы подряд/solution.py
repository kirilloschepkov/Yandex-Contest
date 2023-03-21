def f(l: int) -> int:
    dp = [0] * (l + 4)
    dp[1], dp[2], dp[3] = 2, 4, 7
    for i in range(4, l+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    return dp[l]


print(f(int(input())))
