def f(rows, columns: int) -> int:
    dp = [[0 for _ in range(columns + 3)] for _ in range(rows + 3)]
    dp[2][2] = 1
    starti = startj = 2
    while (starti < rows + 1) or (startj < columns + 1):
        if startj == columns + 1:
            starti += 1
        else:
            startj += 1

        i = starti
        j = startj
        while i <= rows + 1 and j >= 2:
            dp[i][j] = dp[i+1][j-2] + dp[i-1][j-2] + dp[i-2][j-1] + dp[i-2][j+1]
            i += 1
            j -= 1
    return dp[-2][-2]


print(str(f(*map(int, input().split()))))
