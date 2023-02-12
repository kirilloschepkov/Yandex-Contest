cnt_trees, cnt_varieties = map(int, input().split())
trees = list(map(int, input().split()))

best = cnt_trees
answer = [1, cnt_trees]
fst = scd = 0
while scd < cnt_trees:
    while scd < cnt_trees and len(set(trees[fst:scd])) != cnt_varieties: scd += 1
    if len(set(trees[fst:scd])) != cnt_varieties: break
    while len(set(trees[fst:scd])) == cnt_varieties: fst += 1
    distance = len(trees[fst-1:scd])
    if distance == cnt_varieties:
        answer = [fst, scd]
        break
    if best > distance:
        best = distance
        answer = [fst, scd]

print(' '.join(map(str, answer)))
