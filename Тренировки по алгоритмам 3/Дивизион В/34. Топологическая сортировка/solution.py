from sys import setrecursionlimit
from threading import stack_size
setrecursionlimit(199999)
stack_size(2122213)


def get_graph(vertexes: int, edges: list) -> dict:
    res = {k: set() for k in range(1, vertexes + 1)}
    for begin, end in edges:
        res.get(begin).add(end)
    return res


def dfs(g, c, n, r):
    c[n] = 1
    for neighbour in g[n]:
        if c[neighbour] == 0:
            if dfs(g, c, neighbour, r):
                return True
        elif c[neighbour] == 1:
            return True
    r.append(n)
    c[n] = 2


def f(count_vertexes: int, edges: list) -> list:
    graph = get_graph(count_vertexes, edges)
    color = dict.fromkeys(graph.keys(), 0)
    res = list()
    for vertex in graph.keys():
        if color[vertex] == 0:
            if dfs(graph, color, vertex, res):
                return [-1]
    return reversed(res)


cnt_vertexes, cnt_edges = map(int, input().split())
print(*f(cnt_vertexes, [tuple(map(int, input().split())) for _ in range(cnt_edges)]))
