def f1(a, b, c, d, e, f: float) -> str:
    if a == 0 and b == 0 and c == 0 and d == 0 and e == 0 and f == 0: return '5'
    if a * d == b * c and a * f != c * e or a == 0 and b == 0 and e != 0 or c == 0 and d == 0 and f != 0 or a == 0 and c == 0 and b * f != d * e or b == 0 and d == 0 and a * f != c * e: return '0'
    if a * d == b * c and a * f == c * e:
        if b == 0 and d == 0:
            if a != 0 and c != 0: return f'3 {e / a}'
            if a == 0 and e == 0: return f'3 {f / c}'
            if c == 0 and f == 0: return f'3 {e / a}'
        if a == 0 and c == 0:
            if b != 0: return f'4 {e / b}'
            if d != 0: return f'4 {f / d}'
        if b != 0: return f'1 {-a / b} {e / b}'
        if d != 0: return f'1 {-c / d} {f / d}'
    return f'2 {(e * d - b * f) / (a * d - b * c)} {(a * f - e * c) / (a * d - b * c)}'

data = [float(input()) for _ in range(6)]
print(f1(*data))
