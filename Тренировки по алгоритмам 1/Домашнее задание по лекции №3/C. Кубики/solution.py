def f(fst: set, scd: set) -> None:
    common = sorted(fst.intersection(scd))
    only_fst_set = sorted(fst.difference(scd))
    only_scd_set = sorted(scd.difference(fst))
    print(len(common))
    print(' '.join([str(i) for i in common]) if len(common) else '')
    print(len(only_fst_set))
    print(' '.join(map(str, only_fst_set) if len(only_fst_set) else ''))
    print(len(only_scd_set))
    print(' '.join(map(str, only_scd_set) if len(only_scd_set) else ''))


cnt_girl, cnt_boy = map(int, input().split())
f(set(int(input()) for _ in range(cnt_girl)), set(int(input()) for _ in range(cnt_boy)))
