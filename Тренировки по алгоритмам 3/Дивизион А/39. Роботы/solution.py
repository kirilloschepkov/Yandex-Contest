def f(cnt_halls, cnt_tunnels, tunnels, cnt_robots, robots):
    arr1, arr2 = [[] for _ in range(cnt_halls)], [[] for _ in range(cnt_halls)]
    for robot in robots:
        fst, scd = [10**9] * cnt_halls, [10**9] * cnt_halls
        fst[robot] = 0
        visited1, visited2 = [False] * cnt_halls, [False] * cnt_halls
        q = [robot]
        visited1[robot] = True
        while q:
            cur = q.pop(0)
            for nextt in tunnels[cur]:
                if not visited1[nextt] and visited2[cur]:
                    visited1[nextt] = True
                    fst[nextt] = scd[cur] + 1
                    q.append(nextt)
                if not visited2[nextt] and visited1[cur]:
                    visited2[nextt] = True
                    scd[nextt] = fst[cur] + 1
                    q.append(nextt)
        for k in range(cnt_halls):
            arr1[k].append(fst[k])
            arr2[k].append(scd[k])

    res1 = min([10**9] + [2 * min(max(arr1[i]), max(arr2[i])) for i in range(n)])
    res2 = 10**9
    for i in range(cnt_halls):
        for j in tunnels[i]:
            max1 = 0
            max2 = 0
            for k in range(len(robots)):
                max1 = max(max1, min(arr1[i][k], arr1[j][k]))
                max2 = max(max2, min(arr2[i][k], arr2[j][k]))
            res2 = min(res2, max1, max2)

    if res1 == 10**9 and res2 == 10**9:
        return -1
    res = min(res1/2, res2 + 0.5)
    return res if res * 10 % 10 > 0 else int(res)


n, k = map(int, input().split())
t = [[] for _ in range(n)]
for _ in range(k):
    b, e = map(lambda x: int(x) - 1, input().split())
    t[b].append(e)
    t[e].append(b)
print(str(f(n, k, t, int(input()), list(map(lambda x: int(x) - 1, input().split())))))
