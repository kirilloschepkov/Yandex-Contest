def get_graph(vertexes: int, edges: list) -> dict:
    res = {k: set() for k in range(1, vertexes + 1)}
    for fst_vertex, scd_vertex in edges:
        res.get(scd_vertex).add(fst_vertex)
    return res


def dfs(g, c, n):
    c.append(n)
    for neighbour in g[n]:
        if neighbour not in c:
            dfs(g, c, neighbour)


def f(count_vertexes, edges: list) -> None:
    graph = get_graph(count_vertexes, edges)
    component = list()
    dfs(graph, component, 1)
    print(*sorted(component))

cnt_vertexes, cnt_edges = map(int, input().split())
f(cnt_vertexes, [tuple(map(int, input().split())) for _ in range(cnt_edges)])
