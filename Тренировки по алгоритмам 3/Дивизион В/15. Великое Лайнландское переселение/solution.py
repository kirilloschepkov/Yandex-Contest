def f(l: list, cnt) -> list:
    st, res = list(), [-1] * cnt
    for i in range(len(l)):
        if len(st) == 0:
            st.append((l[i], i))
            continue
        while len(st) and st[-1][0] > l[i]: res[st.pop()[1]] = i
        st.append((l[i], i))
    return res


length = int(input())
arr = list(map(int, input().split()))
print(*f(arr, length))
