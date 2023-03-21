def f(cnt: int, l: list) -> int:
    best, length = 0, 0
    arr = dict()
    for i in range(len(l)):
        if l[i] not in arr:
            arr[l[i]] = 0
        arr[l[i]] += 1
        length = max(length, arr[l[i]])
        if best - length >= cnt:
            arr[l[i - best]] -= 1
        else:
            best += 1
    return best


changes = int(input())
line = list(input())
print(str(f(changes, line)))
