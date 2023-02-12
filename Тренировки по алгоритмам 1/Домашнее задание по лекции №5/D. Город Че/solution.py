cnt_intervals, distance = map(int, input().split())
intervals = list(map(int, input().split()))

res = fst = scd = 0
while fst <= scd < cnt_intervals:
    while scd < cnt_intervals - 1 and intervals[scd] - intervals[fst] <= distance: scd += 1
    if intervals[scd] - intervals[fst] <= distance and intervals[scd] == intervals[cnt_intervals - 1]: break
    res += cnt_intervals - scd
    fst += 1

print(res)
