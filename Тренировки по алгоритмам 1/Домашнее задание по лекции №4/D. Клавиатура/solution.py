def f(cnt: int, actual_clicks, max_clicks: list) -> None:
   click_count = [0] * cnt
   for click in actual_clicks: click_count[click - 1] += 1
   for i in range(cnt): print('YES' if max_clicks[i] < click_count[i] else 'NO')


n = int(input())
maxClicks = map(int, input().split())
k = int(input())
actualClicks = map(int, input().split())
f(n, actualClicks, maxClicks)