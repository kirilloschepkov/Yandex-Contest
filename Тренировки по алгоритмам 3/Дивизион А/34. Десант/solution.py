from sys import setrecursionlimit 
from threading import stack_size
setrecursionlimit(199999)
stack_size(2122213)


def dfs(graph, visited, now):
    visited[now] = True
    for v in graph[now]:
        if not visited[v]:
            dfs(graph, visited, v)


def f(n: int, m: int, mapp: list) -> int:
    heights = [[] for _ in range(10001)]
    graph = [[] for _ in range(n * m)]
    visited = [False] * (n * m)
    counter = 0
    for i in range(n):
        for j in range(m):
            vertex = i * m + j
            height = mapp[i][j]
            heights[height].append(vertex)
            if j + 1 < m:
                if height <= mapp[i][j + 1]:
                    graph[vertex].append(vertex + 1)
                if height >= mapp[i][j + 1]:
                    graph[vertex + 1].append(vertex)
            if i + 1 < n:
                if height <= mapp[i + 1][j]:
                    graph[vertex].append(vertex + m)
                if height >= mapp[i + 1][j]:
                    graph[vertex + m].append(vertex)
    for height in heights:
        for vertex in height:
            if not visited[vertex]:
                counter += 1
                dfs(graph, visited, vertex)
    return counter


n, m = map(int, input().split())
print(str(f(n, m, [list(map(int, input().split())) for _ in range(n)])))
