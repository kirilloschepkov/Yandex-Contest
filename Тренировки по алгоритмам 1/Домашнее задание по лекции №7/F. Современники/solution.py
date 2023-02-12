import datetime


def f(c):
    events = list()
    for fst_date, scd_date, index in c:
        events.append((fst_date, 1, index + 1))
        events.append((scd_date, -1, index + 1))
    events.sort()

    added = False
    contemporaries = list()
    for event in events:
        if event[1] == 1:
            added = True
            contemporaries.append(event[2])
        elif event[1] == -1:
            if added:
                print(*contemporaries)
                added = False
            contemporaries.remove(event[2])


cnt_people = int(input())
people = list()
for i in range(cnt_people):
    fst_d, fst_m, fst_y, scd_d, scd_m, scd_y = map(int, input().split())
    birth_date, die_date, eighteen, eighty = datetime.date(fst_y, fst_m, fst_d), datetime.date(scd_y, scd_m, scd_d), datetime.date(fst_y + 18, fst_m, fst_d), datetime.date(fst_y + 80, fst_m, fst_d)
    if die_date < eighteen: continue
    people.append((eighteen, eighty if die_date > eighty else die_date, i))

if len(people) == 0: print('0')
else: f(people)
