def f(length, count: int, places: list) -> int:
    places = [0] + places + [length]
    dp = [[0] * (count + 2) for _ in range(count + 2)]
    for j in range(1, len(dp)):
        for i in range(j - 2, -1, -1):
            dp[i][j] = 10**6 
            for k in range(i + 1, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
            dp[i][j] += places[j] - places[i]
    return dp[0][-1]


print(str(f(*map(int, input().split()), list(map(int, input().split())))))
