def insert(h: list, elem: int) -> None:
    h.append(elem)
    index = len(h) - 1
    while index > 0 and h[index] > h[(index - 1) // 2]:
        h[index], h[(index - 1) // 2] = h[(index - 1) // 2], h[index]
        index = (index - 1) // 2


def extract(h: list) -> int:
    res = h[0]
    h[0] = h[-1]
    index = 0
    while index * 2 + 1 < len(h) - 1:
        index_max_child = index * 2 + 1
        if h[index_max_child] < h[index * 2 + 2]:
            index_max_child = index * 2 + 2
        if h[index] < h[index_max_child]:
            h[index], h[index_max_child] = h[index_max_child], h[index]
            index = index_max_child
        else: break
    h.pop()
    return res


def f(c: list) -> str:
    heap = list()
    for command in c:
        insert(heap, int(command.split()[1])) if command[0] == '0' else print(extract(heap))


commands = [input() for _ in range(int(input()))]
f(commands)
