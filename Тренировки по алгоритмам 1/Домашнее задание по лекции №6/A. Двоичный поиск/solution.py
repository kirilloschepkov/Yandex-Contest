def binary_search(elem: int, arr: list) -> bool:
    left, right = 0, len(arr)
    while left < right:
        middle = (left + right) // 2
        if arr[middle] < elem: left = middle + 1
        elif arr[middle] > elem: right = middle
        else: return True
    return False


length_fst, length_scd = map(int, input().split())
fst = list(map(int, input().split()))
scd = list(map(int, input().split()))

for item in scd:
    print('YES' if binary_search(item, fst) else 'NO')

