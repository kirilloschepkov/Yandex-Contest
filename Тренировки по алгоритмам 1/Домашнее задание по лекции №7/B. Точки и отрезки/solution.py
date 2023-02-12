def f(cnt_s, cnt_p, s, p):
    events = list()
    for i in range(cnt_s):
        events.append((min(s[i]), -1))
        events.append((max(s[i]), 1))
    events += [(p[j], 0) for j in range(cnt_p)]
    events.sort()

    res = dict()
    current = 0
    for event in events:
        if event[1] == -1: current += 1
        elif event[1] == 1: current -= 1
        else: res[event[0]] = current

    return ' '.join([str(res[i]) for i in p])


count_segments, count_points = map(int, input().split())
segments = [list(map(int, input().split())) for _ in range(count_segments)]
points = list(map(int, input().split()))

print(f(count_segments, count_points, segments, points))
