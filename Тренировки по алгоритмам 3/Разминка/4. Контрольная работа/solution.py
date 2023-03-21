def f(cnt_students, cnt_options, desk, side: int) -> set:
    place_fst = desk * 2 - side % 2
    if cnt_students < place_fst + cnt_options and place_fst - cnt_options <= 0:
        return [-1]
    place_scd1 = place_fst - cnt_options
    place_scd2 = place_fst + cnt_options
    desk_scd1 = (place_scd1 + 1) // 2
    desk_scd2 = (place_scd2 + 1) // 2
    if abs(desk - desk_scd1) < abs(desk - desk_scd2) or place_scd2 > cnt_students:
        return desk_scd1, 2 - place_scd1 % 2
    else:
        return desk_scd2, 2 - place_scd2 % 2


print(*f(int(input()), int(input()), int(input()), int(input())))
