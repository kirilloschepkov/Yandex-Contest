inf = int(2e9) + 1
lst = [-inf] + [int(x) for x in input().split()] + [-inf]
length = lst.pop(1) + 2
right, left = [0] * length, [0] * length

st = [0]
for i in range(1, length):
    while lst[st[-1]] > lst[i]: right[st.pop()] = i
    st.append(i)

st = [length - 1]
for i in range(length - 2, 0, -1):
    while lst[st[-1]] > lst[i]: left[st.pop()] = i
    st.append(i)

print(max(lst[i] * (abs(right[i] - left[i] - 1)) for i in range(length)))