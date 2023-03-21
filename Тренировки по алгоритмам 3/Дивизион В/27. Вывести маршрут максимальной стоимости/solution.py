from sys import maxsize


def f(m: list) -> None:
    dp = [[0 for _ in range(len(m[0]))] for _ in range(len(m))]
    for i in range(len(m)):
        for j in range(len(m[0])):
            value_top = dp[i-1][j] if i > 0 else 0
            value_left = dp[i][j-1] if j > 0 else 0
            if value_left == maxsize and value_top == maxsize:
                dp[i][j] = m[i][j]
                continue
            dp[i][j] = max(value_top, value_left) + m[i][j]
    route = list()
    i, j = len(dp) - 1, len(dp[0]) - 1
    while i != 0 or j != 0:
        value_top = dp[i - 1][j] if i > 0 else 0
        value_left = dp[i][j - 1] if j > 0 else 0
        if value_top >= value_left:
            route.append('D')
            i -= 1
        else:
            route.append('R')
            j -= 1
    print(dp[-1][-1])
    print(*reversed(route))


cnt_rows, cnt_columns = map(int, input().split())
matrix = tuple(tuple(map(int, input().split())) for _ in range(cnt_rows))

f(matrix)
