def get_graph(vertexes: int, edges: list) -> dict:
    res = {k: set() for k in range(1, vertexes + 1)}
    for fst_vertex, scd_vertex in edges:
        res.get(fst_vertex).add(scd_vertex)
        res.get(scd_vertex).add(fst_vertex)
    return res


def dfs(g, p, n, part):
    p[n] = part
    for neighbour in g[n]:
        if p[neighbour] == 0:
            if not dfs(g, p, neighbour, 3 - part):
                return False
        elif p[neighbour] == part:
            return False
    return True


def f(count_vertexes: int, edges: list) -> bool:
    graph = get_graph(count_vertexes, edges)
    parts = dict.fromkeys(graph.keys(), 0)
    for vertex in graph.keys():
        if parts[vertex] == 0:
            if not dfs(graph, parts, vertex, 1):
                return False
    return True


cnt_vertexes, cnt_edges = map(int, input().split())
print('YES' if f(cnt_vertexes, [tuple(map(int, input().split())) for _ in range(cnt_edges)]) else 'NO')
