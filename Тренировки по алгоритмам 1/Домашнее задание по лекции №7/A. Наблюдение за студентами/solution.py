def f(cnt_s, cnt_o, v):
    events = list()
    for i in range(cnt_o):
        events.append((v[i][0], -1))
        events.append((v[i][1], 1))
    events.append((cnt_s + 1, -1))
    events.append((cnt_s + 1, 1))
    events.sort()

    res = views = prev = 0
    for i in range(len(events)):
        if views == 0: res += events[i][0] - prev - 1
        if events[i][1] == 1:
            prev = events[i][0]
            views -= 1
        else: views += 1

    return res


count_students, count_observer = map(int, input().split())
views_observer = [tuple(map(int, input().split())) for _ in range(count_observer)]

print(f(count_students, count_observer, views_observer))
