def f(actions: list) -> str:
    res, fst_part, scd_part = list(), list(), list()
    for i in range(len(actions)):
        if actions[i][0] == '+':
            scd_part.append(actions[i].split()[-1])
        elif actions[i][0] == '*':
            fst_part.append(actions[i].split()[-1])

        if i % 2 == 0:
            res.append(fst_part.pop() if fst_part else scd_part.pop(0))

    res += reversed(fst_part)
    res += scd_part
    return '\n'.join([res[i] for i in range(actions.count('-'))])


print(f([input() for _ in range(int(input()))]))
