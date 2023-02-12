cnt_rooms = int(input())
rooms = list(map(int, input().split()))
powers = [0] * 1001
for room in rooms: powers[room] += 1

cnt_conditioners = int(input())
conditioners = dict()
for _ in range(cnt_conditioners):
    power, cost = map(int, input().split())
    if conditioners.get(power, 1001) > cost: conditioners[power] = cost

rev_cond = dict()
for power, cost in conditioners.items():
    temp = list()
    for k in conditioners.keys():
        if conditioners[k] == cost: temp.append(k)
    rev_cond[cost] = max(temp)
sorted_costs_conditioners = sorted(rev_cond)

common_cost = 0
i_cost = 0
for i in range(len(powers)):
    while powers[i] != 0 and i_cost < len(sorted_costs_conditioners) and conditioners[sorted_costs_conditioners[i_cost]] < i: i_cost += 1
    common_cost += sorted_costs_conditioners[i_cost] * powers[i]

print(common_cost)
