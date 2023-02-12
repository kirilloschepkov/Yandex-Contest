from sys import stdin


sales = dict()
for line in stdin.readlines():
    person, product, amount = line.split()
    if sales.get(person) is None:
        sales[person] = dict()
    sales[person][product] = sales[person].get(product, 0) + int(amount)

sales = [(s, sorted([(j, sales[s][j]) for j in sales[s]])) for s in sales]

for person in sorted(sales):
    print(person[0], end=":\n")
    for p in person[1]: print(*p)