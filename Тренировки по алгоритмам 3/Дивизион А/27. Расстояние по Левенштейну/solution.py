def f(fst, scd: str) -> int:
    dp = [[0] * (len(scd) + 1) for _ in range(len(fst) + 1)]
    for i in range(len(fst) + 1): dp[i][0] = i
    for j in range(len(scd) + 1): dp[0][j] = j
    for i in range(1, len(fst) + 1):
        for j in range(1, len(scd) + 1):
            dp[i][j] = min(dp[i][j-1] + 1, dp[i-1][j] + 1, dp[i-1][j-1] + int(fst[i - 1] != scd[j - 1]))
    return dp[-1][-1]

print(str(f(input(), input())))
