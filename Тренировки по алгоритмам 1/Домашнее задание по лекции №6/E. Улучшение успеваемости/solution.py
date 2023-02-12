from math import ceil

a = int(input())
b = int(input())
c = int(input())

print(0 if a == 0 and b == 0 else ceil(a + b / 3 - c / 3))
