def f(l: list) -> bool:
    st = list()
    checker = 1
    for i in range(len(l)):
        while len(st) and st[-1] < l[i]:
            if checker != st.pop():
                return False
            checker += 1
        st.append(l[i])
    return True


input()
arr = list(map(int, input().split()))
print('YES' if f(arr) else 'NO')
