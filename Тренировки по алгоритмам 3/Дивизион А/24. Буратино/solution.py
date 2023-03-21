import datetime


def s(arr: list, target: int):
    l, r = 0, len(arr) - 1
    while l <= r:
        m = (l + r) // 2
        if arr[m] < target:
            l = m + 1
        elif arr[m] > target:
            r = m - 1
        else:
            return m
    return r


def f(l: list) -> int:
    times = list()
    productivity = list()
    for i in range(len(l)):
        hours, minutes, seconds = map(int, l[i][0].split(':'))
        times.append(datetime.timedelta(hours=hours-9, minutes=minutes, seconds=seconds).seconds)
        productivity.append(int(l[i][1]))

    dp_before = [0] * 14401
    for i in range(14401):
        current_productivity = productivity[s(times, i)]
        if i > 0:
            dp_before[i] = max(dp_before[i-1], dp_before[i])
        if i + current_productivity < 14401:
            dp_before[i + current_productivity] = max(dp_before[i + current_productivity], dp_before[i] + 1)

    dp_after = [0] * 14401
    for i in range(14401):
        current_productivity = productivity[s(times, i + 18000)]
        if i > 0:
            dp_after[i] = max(dp_after[i-1], dp_after[i])
        if i + current_productivity < 14401:
            dp_after[i + current_productivity] = max(dp_after[i + current_productivity], dp_after[i] + 1)

    return max(dp_before) + max(dp_after)


print(str(f([input().split() for i in range(int(input()))])))
