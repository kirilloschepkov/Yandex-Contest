cnt, length = map(int, input().split())
sequences = [list(map(int, input().split())) for _ in range(cnt)]

for i in range(len(sequences)):
    for j in range(i + 1, len(sequences)):
        fst = scd = lst = 0
        for _ in range(length):
            if sequences[i][fst] <= sequences[j][scd]: lst, fst = sequences[i][fst], fst + 1
            else: lst, scd = sequences[j][scd], scd + 1
        print(lst)