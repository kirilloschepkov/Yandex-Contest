def binary_search(w, h, c: int) -> int:
    left, right = 0, min(w, h) * c
    while left + 1 < right:
        middle = (left + right) // 2
        if (middle // w) * (middle // h) >= c: right = middle
        else: left = middle
    return right


print(str(binary_search(*map(int, input().split()))))
