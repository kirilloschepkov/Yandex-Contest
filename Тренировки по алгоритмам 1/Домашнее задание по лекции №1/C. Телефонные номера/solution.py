def f(num: str) -> str:
    num = num.replace('-', '').replace('+', '').replace('(', '').replace(')', '')
    return '495' + num if len(num) == 7 else num[1:]


basic_n = f(input())
for _ in range(3):
    print('YES' if f(input()) == basic_n else 'NO')