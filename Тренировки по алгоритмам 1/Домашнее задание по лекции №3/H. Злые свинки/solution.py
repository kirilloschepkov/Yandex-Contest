cnt = int(input())
cnt_y = set()
for _ in range(cnt):
    x, y = map(int, input().split())
    cnt_y.add(x)

print(len(cnt_y))
