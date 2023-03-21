from heapq import heappush, heappop


def f(t: list, cnt: int) -> str:
    events = list()
    for i, time in enumerate(t):
        t_in, t_out = time
        events.append((t_in, -1, i))
        events.append((t_out, 1, i))
    events.sort()

    indexes, ends, res = list(range(cnt)), [-1] * cnt, [0] * len(t)
    for event in events:
        if event[1] == -1:
            try:
                num_end = heappop(indexes)
            except IndexError:
                return f'0 {event[2] + 1}'
            ends[num_end] = event[2]
        elif event[1] == 1:
            num_end = ends.index(event[2])
            res[event[2]] = num_end + 1
            heappush(indexes, num_end)
    return '\n'.join(map(str, res))


cnt_ends, cnt_trains = map(int, input().split())
trains = [tuple(map(int, input().split())) for _ in range(cnt_trains)]
print(f(trains, cnt_ends))
