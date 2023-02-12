def check(diff, people, cnt_people, cnt_teams, cnt_people_in_team):
    fst, scd = 0, cnt_people_in_team - 1
    counter = 0
    while scd < cnt_people:
        if people[scd] - people[fst] <= diff:
            counter += 1
            fst += cnt_people_in_team
            scd += cnt_people_in_team
        else:
            fst += 1
            scd += 1
    return counter >= cnt_teams


def binary_search(p, c, t, pt):
    if pt == 1: return 0
    left, right = -1, p[-1] - p[0]
    while left + 1 < right:
        middle = (left + right) // 2
        if check(middle, p, c, t, pt): right = middle
        else: left = middle
    return right


cnt_people, cnt_teams, cnt_people_in_team = map(int, input().split())
people = sorted([int(input()) for _ in range(cnt_people)])
print(binary_search(people, cnt_people, cnt_teams, cnt_people_in_team))
