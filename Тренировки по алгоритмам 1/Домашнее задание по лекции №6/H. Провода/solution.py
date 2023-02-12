def binary_search(s: list, c: int) -> int:
    left, right = 0, sum(s) // c + 1
    while left + 1 < right:
        middle = (left + right) // 2
        if sum(item // middle for item in s) >= c: left = middle
        else: right = middle
    return left


cnt, cnt_segments = map(int, input().split())
segments = [int(input()) for _ in range(cnt)]
print(str(binary_search(segments, cnt_segments)))
