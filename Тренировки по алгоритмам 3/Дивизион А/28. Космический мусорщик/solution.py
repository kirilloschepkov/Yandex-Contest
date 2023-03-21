def f(commands: list, dir, param: str) -> int:
    direction = ['N', 'S', 'W', 'E', 'U', 'D']

    directions = [-1] * (1 + ord('Z'))
    for i in range(6):
        directions[ord(direction[i])] = i

    counts = [[0] * 6 for _ in range(6)]
    for i in range(6):
        for c in commands[i]:
            counts[i][directions[ord(c)]] += 1

    dp = [[1] * 6 for _ in range(int(param) + 1)]
    for par in range(2, int(param) + 1):
        for prev_dir in range(6):
            for cur_dir in range(6):
                dp[par][prev_dir] += dp[par-1][cur_dir] * counts[prev_dir][cur_dir]
    return dp[int(param)][directions[ord(dir)]]


print(str(f([input() for _ in range(6)], *input().split())))
