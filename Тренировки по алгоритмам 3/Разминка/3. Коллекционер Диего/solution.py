def f(s: set, c: list) -> int:
    res = [-1] * len(c)
    ind = 0
    arr = list()
    for collector in c:
        arr.append((collector, ind))
        ind += 1
    arr.sort()
    fst = scd = 0
    while fst < len(arr):
        while scd < len(s) and arr[fst][0] > s[scd]:
            scd += 1
        res[arr[fst][1]] = scd
        fst += 1
    print('\n'.join(map(str, res)))


cnt_stickers = int(input())
stickers = sorted(set(map(int, input().split())))
cnt_collectors = int(input())
collectors = list(map(int, input().split()))
f(stickers, collectors)

