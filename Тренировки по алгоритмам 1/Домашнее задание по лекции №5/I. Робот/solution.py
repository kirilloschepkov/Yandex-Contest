def f(m: int, o: list) -> int:
    res, cnt = 0, 0
    for i in range(m, len(o)):
        cnt = 0 if o[i] != o[i-m] else cnt + 1
        res += cnt
    return res


memory = int(input())
operations = list(input())
print(str(f(memory, operations)))
