from typing import Optional


def f(d: dict, t: str) -> Optional[str]:
    return d.get(t, None)


cnt = int(input())
dct = dict()
for _ in range(cnt):
    n1, n2 = input().split()
    dct[n1] = n2
    dct[n2] = n1

target = input()
print(f(dct, target))
