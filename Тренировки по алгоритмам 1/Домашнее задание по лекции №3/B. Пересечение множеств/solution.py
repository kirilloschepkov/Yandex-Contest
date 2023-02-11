def f(fst_set: set, scd_set: set) -> str:
    return ' '.join(map(str, sorted(fst_set.intersection(scd_set))))


print(f(set(map(int, input().split())), set(map(int, input().split()))))
