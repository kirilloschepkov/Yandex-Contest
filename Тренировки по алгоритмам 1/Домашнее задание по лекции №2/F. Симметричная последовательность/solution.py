def f(lst: list):
    for i in range(len(lst)):
        if lst[i:] == lst[i:][::-1]:
            return f'{str(i)}\n{" ".join(list(map(str, lst[:i][::-1])))}'


input()
print(f(list(map(int, input().split()))))