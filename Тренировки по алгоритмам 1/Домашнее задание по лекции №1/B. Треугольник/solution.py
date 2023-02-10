def f(input_data: str) -> bool:
    fst_num, scd_num, thd_num = map(int, input_data.split())
    if fst_num + scd_num > thd_num and scd_num + thd_num > fst_num and fst_num + thd_num > scd_num:
        return True
    return False


print('YES' if f(input()) else 'NO')
