def add_one(n: int) -> float:
    if n / 1000 != 9:
        return n + 1000
    return n


def minus_one(n: int) -> float:
    if n % 10 != 1:
        return n - 1
    return n


def shift_left(n: int) -> float:
    return (n % 1000) * 10 + n / 1000


def shift_right(n: int) -> float:
    return (n % 10) * 1000 + n / 10


def bfs(start, stop: int) -> None:
    global d, visited, prev
    d.insert(0, start)
    visited[start] = True
    functions = [add_one, minus_one, shift_left, shift_right]
    while d:
        u = d.pop(0)
        if u == stop:
            return
        for i in range(len(functions)):
            v = int(functions[i](u))
            if v < 10000 and not visited[v]:
                visited[v] = True
                prev[v] = u
                d.append(v)


def path(n: int) -> None:
    global prev
    if n == -1:
        return
    path(prev[n])
    print(n)


def f(fst, scd: int) -> None:
    bfs(fst, scd)
    path(scd)


d = list()
visited = [False] * 10000
prev = [-1] * 10000
f(int(input()), int(input()))
