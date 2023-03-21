def counting(s: list) -> int:
    st = list()
    for char in s:
        if char[-1].isdigit(): st.append(int(char))
        else:
            fst = st.pop()
            scd = st.pop()
            if char == '*': res = fst * scd
            elif char == '+': res = fst + scd
            else: res = scd - fst
            st.append(res)
    return st.pop()


def f(s: str) -> str:
    st, postfix = list(), list()
    last_add, digit = 'op', ''
    for char in list(s):
        if char.isdigit():
            if last_add == ')' or last_add == 'num': return 'WRONG'
            digit += char
        else:
            if digit:
                postfix.append(digit)
                last_add, digit = 'num', ''
            if char == '(':
                if last_add == 'num': return 'WRONG'
                st.append(char)
                last_add = '('
            elif char == ')':
                if last_add == 'op': return 'WRONG'
                while len(st) and st[-1] != '(': postfix.append(st.pop())
                if len(st) == 0: return 'WRONG'
                st.pop()
                last_add = ')'
            elif char == '*':
                if last_add == 'op' or last_add == '(': return 'WRONG'
                while len(st) and st[-1] != '+' and st[-1] != '-' and st[-1] != '(': postfix.append(st.pop())
                st.append(char)
                last_add = 'op'
            elif char == '+':
                if last_add == 'op' or last_add == '(': return 'WRONG'
                while len(st) and st[-1] != '(': postfix.append(st.pop())
                st.append(char)
                last_add = 'op'
            elif char == '-':
                if last_add == 'op' or last_add == '(': postfix.append('0')
                while len(st) and st[-1] != '(': postfix.append(st.pop())
                st.append(char)
                last_add = 'op'
    if digit:
        postfix.append(digit)
        last_add = 'num'
    if last_add == 'op' or last_add == '(': return 'WRONG'
    while st:
        if st[-1] == '(':
            return 'WRONG'
        postfix.append(st.pop())
    # print(postfix)
    return counting(postfix)


print(f(input()))
