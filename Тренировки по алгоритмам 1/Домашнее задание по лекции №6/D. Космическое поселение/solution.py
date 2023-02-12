def binary_search(c, w, h, f_w, f_h: int) -> int:
    left, right = 0, min(f_w, f_h)
    while left + 1 < right:
        middle = (left + right) // 2
        if max((f_w // (h + 2 * middle)) * (f_h // (w + 2 * middle)), (f_w // (w + 2 * middle)) * (f_h // (h + 2 * middle))) >= c: left = middle
        else: right = middle
    return left


print(str(binary_search(*map(int, input().split()))))