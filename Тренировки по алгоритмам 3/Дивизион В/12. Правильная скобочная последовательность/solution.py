def f(s: str) -> bool:
    st = list()
    for char in list(s):
        if char == '(' or char == '{' or char == '[': st.append(char)
        elif len(st):
            last = st.pop()
            if char == ')' and last != '(' or char == '}' and last != '{' or char == ']' and last != '[': return False
        else: return False
    return len(st) == 0


line = input()
print('yes' if f(line) else 'no')
