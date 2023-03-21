def f(fst, scd: list) -> str:
    counter = 0
    while fst and scd and counter < 10**6:
        fst_card, scd_card = fst.pop(0), scd.pop(0)
        if fst_card == 0 and scd_card == 9:
            fst.append(fst_card)
            fst.append(scd_card)
        elif fst_card == 9 and scd_card == 0:
            scd.append(fst_card)
            scd.append(scd_card)
        elif fst_card > scd_card:
            fst.append(fst_card)
            fst.append(scd_card)
        else:
            scd.append(fst_card)
            scd.append(scd_card)
        counter += 1
    if counter == 10**6:
        return 'botva'
    return f'{"first" if fst else "second"} {counter}'


fst_cards = list(map(int, input().split()))
scd_cards = list(map(int, input().split()))
print(f(fst_cards, scd_cards))
