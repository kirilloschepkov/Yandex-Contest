def f(nums: list) -> str:
    return str(len(set(nums)))


print(f(map(int, input().split())))
