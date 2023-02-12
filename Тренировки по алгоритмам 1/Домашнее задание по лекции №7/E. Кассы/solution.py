def f(c, cnt):
    events = list()
    for i, cashier in enumerate(c):
        events.append((cashier[0], -1, i))
        events.append((cashier[1], 1, i))
    events.sort()

    active_cashier = list()
    for event in events:
        if event[1] == -1: active_cashier.append(event[2])
        elif event[1] == 1 and event[2] in active_cashier: active_cashier.remove(event[2])

    res = 0
    for i in range(len(events)):
        if events[i][1] == -1: active_cashier.append(events[i][2])
        elif events[i][1] == 1:
            if cnt == len(active_cashier): res += 1440 - events[i - 1][0] + events[i][0] if i == 0 else events[i][0] - events[i-1][0]
            active_cashier.remove(events[i][2])
    return str(abs(res))


cnt_cashier = int(input())
cashiers = list()
cnt_around = 0
for _ in range(cnt_cashier):
    start_hours, start_minutes, stop_hours, stop_minutes = map(int, input().split())
    if start_hours == stop_hours and start_minutes == stop_minutes:
        cnt_around += 1
        continue
    cashiers.append((start_hours * 60 + start_minutes, stop_hours * 60 + stop_minutes))

if cnt_around == cnt_cashier: print('1440')
elif cnt_cashier == 0: print('0')
else: print(f(cashiers, cnt_cashier - cnt_around))
