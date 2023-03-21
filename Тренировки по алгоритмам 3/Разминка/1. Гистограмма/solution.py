def f(symbols: list) -> None:
    cnt_symbols = dict()
    for s in symbols:
        if s == ' ' or s == '\n': continue
        cnt_symbols[s] = cnt_symbols.get(s, 0) + 1
    sorted_symbols = sorted(cnt_symbols.keys())
    for row in range(max(cnt_symbols.values()), 0, -1):
        for s in sorted_symbols:
            print('#' if cnt_symbols[s] >= row else ' ', end='')
        print()
    print(''.join(sorted_symbols))


line = list(open('input.txt').read())
f(line)