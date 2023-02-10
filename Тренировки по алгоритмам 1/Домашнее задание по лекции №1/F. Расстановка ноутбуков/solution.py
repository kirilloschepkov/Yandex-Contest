def f(x1, y1, x2, y2: int) -> str:
    fst = (x1, y1)
    scd = (x2, y2)
    res = list()
    for i in range(2):
        for j in range(2):
            x = (fst[i] + scd[j])
            y = max(fst[1 if i == 0 else 0], scd[1 if j == 0 else 0])
            res.append((x * y, x, y))
    res.sort(key=lambda x: x[0])
    return ' '.join(map(str, [res[0][1], res[0][2]]))

print(f(*map(int, input().split())))
