def f(nums: list) -> str:
    if len(nums) == 3:
        return ' '.join(map(str, nums))

    max1_pos_num = nums[0]
    min1_neg_num = nums[0]
    for n in nums:
        if n > max1_pos_num: max1_pos_num = n
        if n < min1_neg_num: min1_neg_num = n
    nums.remove(max1_pos_num)
    nums.remove(min1_neg_num)

    max2_pos_num = nums[0]
    min2_neg_num = nums[0]
    for n in nums:
        if n > max2_pos_num: max2_pos_num = n
        if n < min2_neg_num: min2_neg_num = n
    nums.remove(max2_pos_num)

    max3_pos_num = nums[0]
    for n in nums:
        if n > max3_pos_num: max3_pos_num = n

    pos = max1_pos_num * max2_pos_num * max3_pos_num
    neg = min1_neg_num * min2_neg_num * max1_pos_num
    if pos < neg:
        return ' '.join(map(str, (min1_neg_num, min2_neg_num, max1_pos_num)))
    return ' '.join(map(str, [max1_pos_num, max2_pos_num, max3_pos_num]))


print(f(list(map(int, input().split()))))
