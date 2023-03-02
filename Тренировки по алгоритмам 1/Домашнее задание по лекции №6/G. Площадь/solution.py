def binary_search(h, w, c) -> int:
    left, right = -1, min(h, w) // 2 + 1
    while left + 1 < right:
        middle = (left + right)
        if middle * (w + h - middle) <= c: left = middle
        else: right = middle
    return left


height, width, cnt_tile = int(input()), int(input()), int(input())
print(str(binary_search(height, width, cnt_tile)))
