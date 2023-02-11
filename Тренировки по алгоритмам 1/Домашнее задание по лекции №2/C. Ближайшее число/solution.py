def f(nums: list, target: int) -> str:
    diff = 1000
    answer = -1 * target
    for n in nums:
        cur_diff = abs(target - n)
        if cur_diff < diff:
            answer = n
            diff = cur_diff
    return str(answer)


input()
print(f(list(map(int, input().split())), int(input())))
