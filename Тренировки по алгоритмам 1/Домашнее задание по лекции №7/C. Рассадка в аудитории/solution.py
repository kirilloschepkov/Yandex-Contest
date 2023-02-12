def f(cnt_s, d, s):
    events = list()
    for i in range(cnt_s):
        events.append((s[i], -1))
        events.append((s[i] + d, 1))
    events.sort()

    res = 0
    current = 0
    for i in range(len(events)):
        res = max(res, current)
        if events[i][1] == -1: current += 1
        elif events[i][1] == 1: current -= 1

    options = dict()
    option = 1
    for i in sorted(s):
        temp = option % res
        options[i] = temp if temp else res
        option += 1

    print(res)
    for i in s:
        print(options[i], end=' ')


count_students, distance = map(int, input().split())
students = list(map(int, input().split()))
f(count_students, distance, students)
