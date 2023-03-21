def f(m: list, b: int, e: int) -> int:
    visited = [False] * len(m)
    length, prev = [0] * len(m), [-1] * len(m)
    b, e = b - 1, e - 1
    q = [b]
    visited[b] = True
    while q:
        current = q.pop(0)
        for i in range(len(m)):
            if m[current][i] and not visited[i]:
                length[i] = length[current] + 1
                prev[i] = current
                q.append(i)
                visited[i] = True
    if not visited[e]:
        print('-1')
        return
    print(length[e])
    if length[e] > 0: 
        order = list()
        i = e
        while i != -1:
            order.append(i)
            i = prev[i]
        print(*reversed(list(map(lambda x: x+1, order))))


n = int(input())
f([list(map(int, input().split())) for _ in range(n)], *map(int, input().split()))
