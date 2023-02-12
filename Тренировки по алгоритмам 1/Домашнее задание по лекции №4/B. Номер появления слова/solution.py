def f(arr: list) -> None:
    dct = dict()
    for item in arr:
        if item not in dct: dct[item] = 0
        print(str(dct[item]))
        dct[item] += 1


words = open('input.txt').read().split()
f(words)
