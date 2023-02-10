def f(a, b, c: int) -> str:
    if a == b == c == 0: return 'MANY SOLUTIONS'
    if c < 0: return 'NO SOLUTION'
    if a == 0:
        if b == c * c: return 'MANY SOLUTIONS'
        return 'NO SOLUTION'
    if (c * c - b) / a == (c * c - b) // a:
        return str((c * c - b) // a)
    return 'NO SOLUTION'


print(f(int(input()), int(input()), int(input())))
