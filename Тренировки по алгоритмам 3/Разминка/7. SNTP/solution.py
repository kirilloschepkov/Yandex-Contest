from datetime import timedelta, time
from math import ceil


def f(a, b, c: datetime) -> str:
    delta = ceil(datetime.timedelta(hours=c.hour - a.hour, minutes=c.minute - a.minute, seconds=c.second - a.second).seconds / 2)
    res = timedelta(hours=b.hour, minutes=b.minute, seconds=b.second + delta).seconds
    return time(hour=res // 3600 % 60, minute=res // 60 % 60, second=res % 60)


print(f(time(*map(int, input().split(':'))), time(*map(int, input().split(':'))), time(*map(int, input().split(':')))))
