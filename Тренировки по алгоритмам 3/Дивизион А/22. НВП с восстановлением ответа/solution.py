def f(l: list) -> str:
    dp = [0] * len(l)
    dp[0] = 1
    prev = [-1] * len(l)
    for i in range(1, len(l)):
        index = -1
        for j in range(i):
            if l[j] < l[i] and (index >= 0 and dp[j] > dp[index] or index == -1):
                index = j
        dp[i] = dp[index] + 1
        prev[i] = index

    order = list()
    cur = 0
    for i in range(len(dp)):
        if dp[i] > dp[cur]:
            cur = i
    while cur >= 0:
        order.append(l[cur])
        cur = prev[cur]
    return reversed(order)


input()
print(*f(list(map(int, input().split()))))
