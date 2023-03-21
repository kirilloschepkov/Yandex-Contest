def f(rows, columns: int) -> int:
    dp = [[0 for _ in range(columns)] for _ in range(rows)]
    dp[0][0] = 1
    for i in range(rows):
        for j in range(columns):
            dp[i][j] += sum(dp[i-di][j-dj] for di, dj in [(2, 1), (1, 2)] if i - di >= 0 and j - dj >= 0)
    return dp[-1][-1]


print(str(f(*map(int, input().split()))))
