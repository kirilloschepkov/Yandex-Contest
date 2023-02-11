def f(nums: list) -> str:
    return 'NO' if [nums[i-1] >= nums[i] for i in range(1, len(nums))].count(True) else 'YES'


print(f(list(map(int, input().split()))))
