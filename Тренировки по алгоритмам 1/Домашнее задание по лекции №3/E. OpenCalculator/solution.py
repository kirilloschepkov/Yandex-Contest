def f(digits: set, num: set) -> str:
    return str(len(num.difference(digits)))


print(f(set(map(int, input().split())), set(map(int, input().split()))))
