def f(b: list) -> int:
    if len(b) == 1:
        return b[0][0]
    if len(b) == 2:
        return min(b[0][1], b[0][0] + b[1][0])
    dp = [0] * len(b)
    dp[0], dp[1], dp[2] = b[0][0], min(b[0][1], b[0][0] + b[1][0]), min(b[0][2], b[0][0] + b[1][0] + b[2][0], b[0][1] + b[2][0], b[0][0] + b[1][1])
    for i in range(3, len(b)):
        dp[i] = min(dp[i-1] + b[i][0], dp[i-2] + b[i-1][1], dp[i-3] + b[i-2][2])
    return dp[len(b)-1]


print(str(f([list(map(int, input().split())) for _ in range(int(input()))])))
