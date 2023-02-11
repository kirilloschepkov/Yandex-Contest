def f(nums: list) -> str:
    return str(len([i for i in range(1, len(nums) - 1) if nums[i-1] < nums[i] and nums[i+1] < nums[i]]))


print(f(list(map(int, input().split()))))
