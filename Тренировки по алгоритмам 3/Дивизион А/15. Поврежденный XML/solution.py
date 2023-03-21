def check(l: list) -> bool:
    st = list()
    st_tags = list()
    for char in l:
        if char == '<':
            if len(st_tags) != 0: return False
            st_tags.append(char)
        elif char == '>':
            if len(st_tags) != 2 or st_tags[0] != '<': return False
            last_tag = st_tags.pop()
            if list(set(last_tag))[0] == '/' and len(set(last_tag)) == 1:
                return False
            if last_tag[0] == '/':
                if len(st) == 0: return False
                if st.pop() != last_tag[1:]: return False
            else:
                st.append(last_tag)
            st_tags.pop()
        else:
            if len(st_tags) == 0 or st_tags[0] != '<': return False
            elif len(st_tags) == 1: st_tags.append(char)
            else:
                st_tags.append(st_tags.pop() + char)
    return len(st) == 0


def f(s: list) -> str:
    alphabet = set(s)
    alphabet.add('<')
    alphabet.add('>')
    alphabet.add('/')
    for i in range(len(s)):
        temp = s[i]
        for char in alphabet:
            s[i] = char
            if s[0] != '<' or s[-1] != '>':
                continue
            if check(s):
                return ''.join(s)
        s[i] = temp


print(f(list(input())))
