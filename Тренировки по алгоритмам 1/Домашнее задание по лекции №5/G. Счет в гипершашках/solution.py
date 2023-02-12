cnt_cards, diff = map(int, input().split())
cards = list(map(int, input().split()))

cnts_cards = dict()
for card in cards: cnts_cards[card] = cnts_cards.get(card, 0) + 1

unique_cards = sorted(set(cards))
fst = scd = answer = duplicates = 0

while fst < len(unique_cards):
    while scd < len(unique_cards) and unique_cards[fst] * diff >= unique_cards[scd]:
        if cnts_cards[unique_cards[scd]] > 1: duplicates += 1
        scd += 1
    if cnts_cards[unique_cards[fst]] > 1: answer += (scd - fst - 1) * 3
    if cnts_cards[unique_cards[fst]] > 2: answer += 1
    answer += (scd - fst - 1) * (scd - fst - 2) * 3
    if cnts_cards[unique_cards[fst]] > 1: duplicates -= 1
    answer += duplicates * 3
    fst += 1

print(answer)
