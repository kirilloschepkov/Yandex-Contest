def f(s: str) -> int:
    st = list()
    for char in s.strip().split():
        if char.isdigit(): st.append(int(char))
        else:
            fst = st.pop()
            scd = st.pop()
            if char == '*': res = fst * scd
            elif char == '+': res = fst + scd
            else: res = scd - fst
            st.append(res)
    return st.pop()


line = input()
print(str(f(line)))
