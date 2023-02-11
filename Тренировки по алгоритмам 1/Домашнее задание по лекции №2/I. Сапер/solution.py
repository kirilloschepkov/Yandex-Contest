def show(q):
    for row in q:
        for col in row:
            print(col, end=' ')
        print()


def f(field, coords) -> str:
    for x, y in coords: field[x - 1][y - 1] = '*'
    for y in range(len(field)):
        for x in range(len(field[y])):
            if field[y][x] == '*': continue
            for dx, dy in [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]:
                next_x, next_y = x + dx, y + dy
                if next_y < 0 or next_y > len(field) - 1 or next_x < 0 or next_x > len(field[0]) - 1: continue
                if field[next_y][next_x] == '*': field[y][x] += 1
    show(field)


x_size, y_size, cnt_mines = map(int, input().split())
coords_mines = list()
for _ in range(cnt_mines):
    x, y = map(int, input().split())
    coords_mines.append((x, y))

f(field=[[0 for _ in range(y_size)] for _ in range(x_size)], coords=coords_mines)
