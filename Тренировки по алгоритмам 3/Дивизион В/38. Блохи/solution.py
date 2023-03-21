def get_neighbors(x, y, w, h):
    res = list()
    for i in range(-2, 3):
        if i != 0:
            for j in range(-2, 3):
                if j != 0 and abs(i) != abs(j) and 1 <= x + i <= w and 1 <= y + j <= h:
                    res.append((x + i, y + j))
    return res


def f(width, height, x_feeder, y_feeder, coords):
    arr = [[-1] * (height + 1) for _ in range(width + 1)]
    arr[x_feeder][y_feeder] = 0
    queue = [(x_feeder, y_feeder)]
    while queue:
        x, y = queue.pop(0)
        for next_x, next_y in get_neighbors(x, y, width, height):
            if arr[next_x][next_y] == -1:
                arr[next_x][next_y] = arr[x][y] + 1
                queue.append((next_x, next_y))
    counter = 0
    for x, y in coords:
        if arr[x][y] == -1:
            return -1
        counter += arr[x][y]
    return counter


n, m, s, t, q = map(int, input().split())
print(str(f(n, m, s, t, [tuple(map(int, input().split())) for _ in range(q)])))
