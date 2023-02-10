def f(mode: str, temp: str) -> int:
    fst, lst = map(int, temp.split())
    if mode == 'fan': return fst
    if mode == 'auto': return lst
    if mode == 'heat':
        if fst < lst: return lst
        return fst
    if mode == 'freeze':
        if fst > lst: return lst
        return fst


print(str(f(input(), input())))
