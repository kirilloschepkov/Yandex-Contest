def f(line: list, length_line, length_window: int) -> str:
    res = list()
    dequeue = list()
    for i in range(length_line):
        if len(dequeue) > 0 and dequeue[0] <= i - length_window:
            dequeue.pop(0)
        while len(dequeue) > 0 and line[dequeue[-1]] >= line[i]:
            dequeue.pop()
        dequeue.append(i)
        if i >= k - 1:
            res.append(line[dequeue[0]])
    return '\n'.join(map(str, res))


n, k = map(int, input().split())
s = list(map(int, input().split()))
print(f(s, n, k))
