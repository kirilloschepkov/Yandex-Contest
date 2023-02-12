def f(b: list) -> str:
    b.sort(key=lambda x: -x[0])
    dct = dict()
    for w, h in b:
        if w not in dct:
            dct[w] = h
            continue
        if dct[w] < h:
            dct[w] = h
    return str(sum(dct.values()))


blocks = [tuple(map(int, input().split())) for _ in range(int(input()))]
print(f(blocks))
