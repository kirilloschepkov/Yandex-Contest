def f(l: list) -> bool:
    st = list()
    last_added = 0
    for i in range(len(l)):
        while len(st) and st[-1] < l[i]:
            top_st = st.pop()
            if last_added > top_st:
                return False
            last_added = top_st
        st.append(l[i])
    return last_added <= st[-1]


for _ in range(int(input())):
    arr = list(map(float, input().split()))
    print('1' if f(arr[1:]) else '0')
