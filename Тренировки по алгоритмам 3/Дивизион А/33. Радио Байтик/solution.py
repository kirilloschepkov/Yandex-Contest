def f(coords) -> None:
    res = list()
    left, right = 0, 800000001
    while left + 1 < right:
        middle = (left + right) // 2
        colors, st = [0] * len(coords), list()
        flag = True
        for i in range(len(coords)):
            if not flag: break
            if colors[i] == 0:
                st.append(i)
                colors[i] = 1
                while st and flag:
                    cur = st.pop()
                    for j in range(len(coords)):
                        if j != cur and (coords[cur][0] - coords[j][0])**2 + (coords[cur][1] - coords[j][1])**2 < middle:
                            if colors[j] == 0:
                                st.append(j)
                                colors[j] = 3 - colors[cur]
                            elif colors[j] == colors[cur]:
                                flag = False
                                break
        if flag:
            res = colors
            left = middle
        else:
            right = middle
    print(f'{(left**(1/2))/2:.9f}')
    print(*res)


f([tuple(map(int, input().split())) for _ in range(int(input()))])
