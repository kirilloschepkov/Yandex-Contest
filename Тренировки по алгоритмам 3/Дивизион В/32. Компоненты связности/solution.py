def get_graph(vertexes: int, edges: list) -> dict:
    res = {k: set() for k in range(1, vertexes + 1)}
    for fst_vertex, scd_vertex in edges:
        res.get(fst_vertex).add(scd_vertex)
        res.get(scd_vertex).add(fst_vertex)
    return res


def f(count_vertexes: int, edges: list) -> None:
    graph = get_graph(count_vertexes, edges)
    visited = dict.fromkeys(graph.keys(), False)
    components = list()
    for vertex in graph.keys():
        if visited.get(vertex):
            continue
        component = list()
        q = [vertex]
        while q:
            n = q.pop()
            component.append(n)
            for neighbour in graph[n]:
                if not visited[neighbour] and neighbour not in component:
                    visited[neighbour] = True
                    q.append(neighbour)
        components.append(component)

    print(len(components))
    for component in components:
        print(len(component))
        print(*component)

cnt_vertexes, cnt_edges = map(int, input().split())
f(cnt_vertexes, [tuple(map(int, input().split())) for _ in range(cnt_edges)])
