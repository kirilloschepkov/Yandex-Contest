def f(n: int) -> int:
    dp = [10**6] * (n + 1)
    dp[0] = 0
    cubes = [n*n*n for n in range(1, round(n**(1/3)) + 1)]
    for cube in cubes:
        for i in range(cube, n + 1):
            dp[i] = min(dp[i], dp[i-cube] + 1)
    return dp[-1]


print(str(f(int(input()))))
