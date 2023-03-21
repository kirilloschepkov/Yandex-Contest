def f(c: list, cnt: int) -> int:
    if cnt == 1: return 0
    lst = [c[i] for i in range(cnt)]
    return sum([min(lst[i-1], lst[i]) for i in range(1, cnt)])


count = int(input())
chars = [int(input()) for _ in range(count)]
print(str(f(chars, count)))
