def get_graph(edges: list) -> dict:
    res = dict()
    for fst_vertex, scd_vertex in edges:
        res.setdefault(fst_vertex, set())
        res.get(fst_vertex).add(scd_vertex)
        res.setdefault(scd_vertex, set())
        res.get(scd_vertex).add(fst_vertex)
    return res


def dfs(g, c, n):
    c.append(n)
    for neighbour in g[n]:
        if neighbour not in c:
            dfs(g, c, neighbour)


def f(edges: list) -> None:
    if len(edges) == 0:
        print('1', '1', sep='\n')
        return
    graph = get_graph(edges)
    if 1 not in graph.keys():
        print('1', '1', sep='\n')
        return
    component = list()
    dfs(graph, component, 1)
    print(len(component))
    print(*sorted(component))

cnt_vertexes, cnt_edges = map(int, input().split())
f([tuple(map(int, input().split())) for _ in range(cnt_edges)])
