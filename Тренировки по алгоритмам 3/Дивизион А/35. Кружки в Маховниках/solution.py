import heapq


class MaxHeap:
    def __init__(self, data=None):
        if data is None:
            self.data = []
        else:
            self.data = [-i for i in data]
            heapq.heapify(self.data)

    def push(self, item):
        heapq.heappush(self.data, -item)

    def pop(self):
        return -heapq.heappop(self.data)

    def __len__(self):
        return len(self.data)

    def __str__(self):
        return ' '.join(map(str, self.data))


def f(arr: list) -> None:
    arr = [0] + arr
    graph = [[] for _ in range(len(arr))]
    degree = [0] * len(arr)
    for i in range(1, len(arr)):
        for j in range(1, arr[i][0] + 1):
            graph[i].append(arr[i][j])
            degree[arr[i][j]] += 1

    h = [i for i in range(1, len(degree)) if degree[i] == 0]
    max_heap = MaxHeap(h)

    res = list()
    while len(max_heap) > 0:
        v = max_heap.pop()
        res.append(v)
        for i in range(len(graph[v])):
            to = graph[v][i]
            degree[to] -= 1
            if degree[to] == 0:
                max_heap.push(to)

    print(*reversed(res))


f([list(map(int, input().split())) for _ in range(int(input()))])
