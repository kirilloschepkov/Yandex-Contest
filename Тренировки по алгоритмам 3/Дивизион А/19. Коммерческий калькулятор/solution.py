from heapq import heappop, heappush, heapify


def f(n: list) -> int:
    res = 0
    heapify(n)
    while len(n) > 1:
        summ = heappop(n) + heappop(n)
        res += summ * 0.05
        heappush(n, summ)

    return "%.2f" % res


count = int(input())
numbers = list(map(int, input().split()))
print(str(f(numbers)))
