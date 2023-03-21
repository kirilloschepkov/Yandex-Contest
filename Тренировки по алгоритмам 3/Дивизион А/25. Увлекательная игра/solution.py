def f(n, a, b) -> int:
    dp = [0] * (n + 1)
    for i in range(2, n+1):
        dp[i] = min(max(a + dp[j], b + dp[i-j]) for j in range(1, i))
    return dp[-1]


print(str(f(*map(int, input().split()))))
