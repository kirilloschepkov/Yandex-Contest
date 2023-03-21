def counting(s: list) -> bool:
    st = list()
    for char in s:
        if char is True or char is False: st.append(int(char))
        elif char == '!': st.append(not st.pop())
        else:
            fst = st.pop()
            scd = st.pop()
            if char == '&': res = fst and scd
            elif char == '|': res = fst or scd
            else: res = fst ^ scd
            st.append(res)
    return st.pop()


def f(s: str) -> str:
    st, postfix = list(), list()
    for char in list(s):
        if char.isdigit(): postfix.append(True if int(char) > 0 else False)
        else:
            if char == '!':
                while len(st) and st[-1] != '&' and st[-1] != '|' and st[-1] != '^' and st[-1] != '(': postfix.append(st.pop())
                st.append(char)
            elif char == '&':
                while len(st) and st[-1] != '|' and st[-1] != '^' and st[-1] != '(': postfix.append(st.pop())
                st.append(char)
            elif char == '|' or char == '^':
                while len(st) and st[-1] != '(': postfix.append(st.pop())
                st.append(char)
            elif char == '(':
                st.append(char)
            elif char == ')':
                while len(st) and st[-1] != '(': postfix.append(st.pop())
                st.pop()
    while st: postfix.append(st.pop())
    return '1' if counting(postfix) else '0'


print(f(input()))
