def f(fst: str, scd: str) -> int:
    q = list()
    x1, y1 = ord(fst[0]) - ord('a'), ord(fst[1]) - ord('1')
    x2, y2 = ord(scd[0]) - ord('a'), ord(scd[1]) - ord('1')
    fst_field = [[10**6 for _ in range(8)] for _ in range(8)]
    fst_field[x1][y1] = 0
    q.append((x1, y1))
    while q:
        x, y = q.pop(0)
        if x < 6 and y < 7 and fst_field[x + 2][y + 1] == 10**6:
            fst_field[x + 2][y + 1] = fst_field[x][y] + 1
            q.append((x + 2, y + 1))
        if x < 7 and y < 6 and fst_field[x + 1][y + 2] == 10**6:
            fst_field[x + 1][y + 2] = fst_field[x][y] + 1
            q.append((x + 1, y + 2))
        if x < 6 and y > 0 and fst_field[x + 2][y - 1] == 10**6:
            fst_field[x + 2][y - 1] = fst_field[x][y] + 1
            q.append((x + 2, y - 1))
        if x > 0 and y < 6 and fst_field[x - 1][y + 2] == 10**6:
            fst_field[x - 1][y + 2] = fst_field[x][y] + 1
            q.append((x - 1, y + 2))
        if x > 1 and y < 7 and fst_field[x - 2][y + 1] == 10**6:
            fst_field[x - 2][y + 1] = fst_field[x][y] + 1
            q.append((x - 2, y + 1))
        if x < 7 and y > 1 and fst_field[x + 1][y - 2] == 10**6:
            fst_field[x + 1][y - 2] = fst_field[x][y] + 1
            q.append((x + 1, y - 2))
        if x > 0 and y > 1 and fst_field[x - 1][y - 2] == 10**6:
            fst_field[x - 1][y - 2] = fst_field[x][y] + 1
            q.append((x - 1, y - 2))
        if x > 1 and y > 0 and fst_field[x - 2][y - 1] == 10**6:
            fst_field[x - 2][y - 1] = fst_field[x][y] + 1
            q.append((x - 2, y - 1))

    scd_field = [[10 ** 6 for _ in range(8)] for _ in range(8)]
    scd_field[x2][y2] = 0
    q.append((x2, y2))
    while q:
        x, y = q.pop(0)
        if fst_field[x][y] == scd_field[x][y]:
            return fst_field[x][y]
        if x < 6 and y < 7 and scd_field[x + 2][y + 1] == 10**6:
            scd_field[x + 2][y + 1] = scd_field[x][y] + 1
            q.append((x + 2, y + 1))
        if x < 7 and y < 6 and scd_field[x + 1][y + 2] == 10**6:
            scd_field[x + 1][y + 2] = scd_field[x][y] + 1
            q.append((x + 1, y + 2))
        if x < 6 and y > 0 and scd_field[x + 2][y - 1] == 10**6:
            scd_field[x + 2][y - 1] = scd_field[x][y] + 1
            q.append((x + 2, y - 1))
        if x > 0 and y < 6 and scd_field[x - 1][y + 2] == 10**6:
            scd_field[x - 1][y + 2] = scd_field[x][y] + 1
            q.append((x - 1, y + 2))
        if x > 1 and y < 7 and scd_field[x - 2][y + 1] == 10**6:
            scd_field[x - 2][y + 1] = scd_field[x][y] + 1
            q.append((x - 2, y + 1))
        if x < 7 and y > 1 and scd_field[x + 1][y - 2] == 10**6:
            scd_field[x + 1][y - 2] = scd_field[x][y] + 1
            q.append((x + 1, y - 2))
        if x > 0 and y > 1 and scd_field[x - 1][y - 2] == 10**6:
            scd_field[x - 1][y - 2] = scd_field[x][y] + 1
            q.append((x - 1, y - 2))
        if x > 1 and y > 0 and scd_field[x - 2][y - 1] == 10**6:
            scd_field[x - 2][y - 1] = scd_field[x][y] + 1
            q.append((x - 2, y - 1))
    return -1

print(f(*input().split()))
