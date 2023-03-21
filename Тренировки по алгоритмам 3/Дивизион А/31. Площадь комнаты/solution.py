def dfs(m, x, y):
    global count
    if m[x][y] == '*': return
    count += 1
    m[x][y] = '*'
    dfs(m, x-1, y)
    dfs(m, x+1, y)
    dfs(m, x, y-1)
    dfs(m, x, y+1)


def f(maze: list, x, y: int) -> int:
    dfs(maze, x-1, y-1)

count = 0
f([list(input()) for _ in range(int(input()))], *map(int, input().split()))
print(count)
