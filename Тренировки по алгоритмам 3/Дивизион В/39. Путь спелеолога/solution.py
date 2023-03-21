def bfs(b, basic):
    d = [(-1, 0, 0), (1, 0, 0), (0, 0, -1), (0, 0, 1), (0, -1, 0), (0, 1, 0)]
    steps = -1
    b[basic[0]][basic[1]][basic[2]] = 2
    q = [basic]
    while q:
        z, x, y = q.pop(0)
        if z == 0:
            steps = b[z][x][y]
            break
        for i in range(6):
            dz, dx, dy = z + d[i][0], x + d[i][1], y + d[i][2]
            if dz >= 0 and dx >= 0 and dy >= 0 and dz != len(b) and dx != len(b) and dy != len(b) and b[dz][dx][dy] == 0:
                b[dz][dx][dy] = b[z][x][y] + 1
                q.append((dz, dx, dy))
    return steps - 2


def f(b: list) -> int:
    lst = [[[0] * len(b) for _ in range(len(b))] for _ in range(len(b))]
    basic = None
    for i in range(len(b)):
        for j in range(len(b)):
            for k in range(len(b)):
                symbol = b[i][j][k]
                if symbol == 'S':
                    basic = (i, j, k)
                lst[i][j][k] = 1 if symbol == '#' else 0
    return bfs(lst, basic)


n = int(input())
blocks = list()
for _ in range(n):
    input()
    blocks.append([list(input()) for _ in range(n)])

print(str(f(blocks)))
