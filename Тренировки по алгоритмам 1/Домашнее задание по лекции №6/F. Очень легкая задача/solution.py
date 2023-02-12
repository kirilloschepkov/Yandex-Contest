def binary_search(n, x, y: int) -> str:
    left, right = 0, (n - 1) * max(x, y)
    while left + 1 < right:
        middle = (left + right) // 2
        if (1 + middle // x + middle // y) >= n: right = middle
        else: left = middle
    return right + min(x, y)


print(str(binary_search(*map(int, input().split()))))
