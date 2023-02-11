def f(nums: list) -> str:
    res = list()
    mx = max(nums)
    is_after_max = False
    for i in range(len(nums) - 1):
        if nums[i] == mx and not is_after_max:
            is_after_max = True
            continue
        if not is_after_max: continue
        if nums[i] % 10 == 5 and nums[i+1] < nums[i]: res.append(nums[i])
    if not res: return '0'
    nums.sort(key=lambda x: -x)
    return str(nums.index(max(res)) + 1)


input()
print(f(list(map(int, input().split()))))
