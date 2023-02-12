def f(l):
    events = list()
    for i in range(len(l) - 1, 0, -2):
        events.append((l[i - 1], -1))
        events.append((l[i], 1))
    events.sort()
    if 0 < events[0][0] or events[-1][0] < 10000: return False

    security = 0
    solo_security = 0
    prev = -1
    for event in events:
        if security < 1 and event[0] != 0: return False
        if security == 1 and event[0] != prev: solo_security += 1
        if event[1] == -1: security += 1
        elif event[1] == 1: security -= 1
        prev = event[0]

    return False if solo_security != line[0] else True


cnt_lines = int(input())
for _ in range(cnt_lines):
    line = list(map(int, input().split()))
    print('Accepted' if f(line) else 'Wrong Answer')
