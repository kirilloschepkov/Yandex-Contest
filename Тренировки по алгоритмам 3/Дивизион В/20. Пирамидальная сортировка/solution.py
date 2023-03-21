def heapify(heap: list) -> None:
    for i in range(len(heap) // 2 - 1, -1, -1):
        while i * 2 + 1 < len(heap):
            index_max_child = i * 2 + 1
            if i * 2 + 2 < len(heap) and heap[index_max_child] > heap[i * 2 + 2]:
                index_max_child = i * 2 + 2
            if heap[i] > heap[index_max_child]:
                heap[i], heap[index_max_child] = heap[index_max_child], heap[i]
                i = index_max_child
            else:
                break


def extract(h: list) -> int:
    res = h[0]
    h[0], index = h[-1], 0
    while index * 2 + 1 < len(h) - 1:
        index_max_child = index * 2 + 2 if h[index * 2 + 1] > h[index * 2 + 2] else index * 2 + 1
        if h[index] > h[index_max_child]:
            h[index], h[index_max_child] = h[index_max_child], h[index]
            index = index_max_child
        else: break
    h.pop()
    return res


def f(n: list) -> list:
    heapify(n)
    return [extract(n) for _ in range(len(n))]


input()
numbers = list(map(int, input().split()))
print(*f(numbers))
