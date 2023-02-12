def f(arr: list) -> str:
    dct = dict()
    for item in arr: dct[item] = dct.get(item, 0) + 1
    reversed_dct = dict()
    for k, v in dct.items():
        if v not in reversed_dct: reversed_dct[v] = list()
        reversed_dct[v].append(k)
    return str(min(reversed_dct[max(reversed_dct)]))


words = open('input.txt').read().split()
print(f(words))
