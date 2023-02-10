def f(interval_fst, interval_scd, count_fst, count_scd: int) -> str:
    min_fst = interval_fst * (count_fst - 1) + count_fst
    min_scd = interval_scd * (count_scd - 1) + count_scd
    max_fst = min_fst + 2 * interval_fst
    max_scd = min_scd + 2 * interval_scd
    if max(min_fst, min_scd) > min(max_fst, max_scd):
        return '-1'
    return str(max(min_fst, min_scd)) + ' ' + str(min(max_fst, max_scd))


print(f(int(input()), int(input()), int(input()), int(input())))
