from sys import maxsize


def f(m: list) -> int:
    dp = [[0 for _ in range(len(m[0]))] for _ in range(len(m))]
    for i in range(len(m)):
        for j in range(len(m[0])):
            value_top = dp[i-1][j] if i > 0 else maxsize
            value_left = dp[i][j-1] if j > 0 else maxsize
            if value_left == maxsize and value_top == maxsize:
                dp[i][j] = m[i][j]
                continue
            dp[i][j] = min(value_left, value_top) + m[i][j]
    return dp[-1][-1]


cnt_rows, cnt_columns = map(int, input().split())
matrix = tuple(tuple(map(int, input().split())) for _ in range(cnt_rows))

print(str(f(matrix)))
