def f(nums: list) -> str:
    if len(nums) == 2:
        return f'{min(nums)} {max(nums)}'
    max1_pos_num, max2_pos_num, min1_neg_num, min2_neg_num = 0, 0, 0, 0
    for n in nums:
        if n > 0:
            if n >= max1_pos_num:
                max2_pos_num = max1_pos_num
                max1_pos_num = n
            elif n > max2_pos_num: max2_pos_num = n
        elif n < 0:
            if n <= min1_neg_num:
                min2_neg_num = min1_neg_num
                min1_neg_num = n
            elif n < min2_neg_num: min2_neg_num = n
    pos = max1_pos_num * max2_pos_num
    neg = min1_neg_num * min2_neg_num
    return f'{max2_pos_num} {max1_pos_num}' if pos > neg else f'{min1_neg_num} {min2_neg_num}'


print(f(list(map(int, input().split()))))
