def f(r: dict, w: list) -> int:
    return str(len([word for word in w if word.lower() not in r.keys() and len([char for char in word if char != char.lower()]) != 1 or word.lower() in r.keys() and word not in r[word.lower()]]))


rules = dict()
for _ in range(int(input())):
    rule = input()
    if rule.lower() not in rules.keys():
        rules[rule.lower()] = list()
    rules[rule.lower()].append(rule)

line = input()
print(str(f(rules, line.split())))