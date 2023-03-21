def f(target: int) -> str:
    dp = [0] * (target + 1)
    prev = [0] * (target + 1)
    for i in range(2, target + 1):
        min_prev_index = i-1
        if i % 2 == 0 and dp[i//2] < dp[min_prev_index]:
            min_prev_index = i//2
        if i % 3 == 0 and dp[i//3] < dp[min_prev_index]:
            min_prev_index = i//3
        dp[i] = dp[min_prev_index] + 1
        prev[i] = min_prev_index
    order = list()
    cur = target
    while cur:
        order.append(cur)
        cur = prev[cur]
    return f'{dp[target]}\n{" ".join(map(str, reversed(order)))}'


print(f(int(input())))
