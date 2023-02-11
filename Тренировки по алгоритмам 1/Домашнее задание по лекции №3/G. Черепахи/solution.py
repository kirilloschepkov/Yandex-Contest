def f(l: list, cnt: int) -> str:
    return str(len([1 for cnt_before, cnt_after in l if cnt_before >= 0 and cnt_after >= 0 and cnt_before + cnt_after == cnt - 1]))


cnt_turtles = int(input())
print(f([tuple(map(int, input().split())) for _ in range(cnt_turtles)], cnt_turtles))
