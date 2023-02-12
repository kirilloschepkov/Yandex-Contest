def binary_search(elem: int, arr: list) -> int:
    left, right = 0, len(arr)
    while left < right:
        middle = (left + right) // 2
        if arr[middle] < elem: left = middle + 1
        elif arr[middle] > elem: right = middle
        else: return arr[middle]
    if left >= len(arr): return arr[right - 1]
    if right == 0 or arr[right] - elem < elem - arr[left - 1]: return arr[right]
    return arr[left - 1]


input()
fst = list(map(int, input().split()))
scd = list(map(int, input().split()))

for item in scd:
    print(str(binary_search(item, fst)))
