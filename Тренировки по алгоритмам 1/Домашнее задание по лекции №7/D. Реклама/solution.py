def f(cnt, g):
    guests = list()
    for i in range(cnt):
        come, back = g[i]
        if back - come < 5: continue
        guests.append((come, back - 5, i))

    events = list()
    for guest in guests:
        events.append((guest[0], -1, guest[2]))
        events.append((guest[1], 1, guest[2]))
    events.sort()

    fst_start = list()
    fst_current = list()
    fst_views = [[]]
    for event in events:
        if event[1] == -1: fst_current.append(event[2])
        elif event[1] == 1:
            if len(fst_current) > len(fst_views[0]):
                fst_views = [fst_current.copy()]
                fst_start = [event[0]]
            elif len(fst_current) == len(fst_views[0]):
                fst_views.append(fst_current.copy())
                fst_start.append(event[0])
            fst_current.remove(event[2])

    if len(fst_start) == 0: fst_start = [1]

    best = [0, 0, 0]
    for i in range(len(fst_start)):
        fst_start_current, fst_views_current = fst_start[i], fst_views[i]

        scd_start = -1
        scd_cnt = scd_cnt_best = 0
        for event in events:
            if event[1] == -1 and event[2] not in fst_views_current:
                scd_cnt += 1
                if scd_cnt > scd_cnt_best and (event[0] <= fst_start_current - 5 or fst_start_current + 5 <= event[0]):
                    scd_cnt_best = scd_cnt
                    scd_start = event[0]
            elif event[1] == 1 and event[2] not in fst_views_current:
                if scd_cnt > scd_cnt_best and (event[0] <= fst_start_current - 5 or fst_start_current + 5 <= event[0]):
                    scd_cnt_best = scd_cnt
                    scd_start = event[0]
                scd_cnt -= 1

        if scd_start == -1: scd_start = fst_start_current + 6
        elif fst_start_current > scd_start:
            fst_start_current, scd_start = scd_start, fst_start_current

        counter = len(fst_views_current) + scd_cnt_best
        if counter > best[0]: best = [counter, fst_start_current, scd_start]

    return ' '.join(map(str, best))


count_guests = int(input())
guests = [list(map(int, input().split())) for _ in range(count_guests)]

print(f(count_guests, guests))
