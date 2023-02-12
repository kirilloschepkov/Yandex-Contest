cnt_points = int(input())
forward = [0, 0]
back = [0, 0]
x_prev = y_prev = -1

while cnt_points:
    x, y = map(int, input().split())
    if x_prev == -1: pass
    elif y > y_prev:
        forward.append(forward[-1] + y - y_prev)
        back.append(back[-1])
    else:
        forward.append(forward[-1])
        back.append(back[-1] + y_prev - y)
    x_prev = x
    y_prev = y
    cnt_points -= 1

cnt_track = int(input())
while cnt_track:
    start, end = map(int, input().split())
    print(forward[end] - forward[start] if start < end else back[start] - back[end])
    cnt_track -= 1
