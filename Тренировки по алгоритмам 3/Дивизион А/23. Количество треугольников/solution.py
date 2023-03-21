def f(level: int) -> int:
    k = level // 2
    if level % 2 == 0:
        res = k * (k + 1) * (4 * k + 1) // 2
    else:
        res = (k + 1) * (4 * k * k + 7 * k + 2) // 2
    return res


print(str(f(int(input()))))
