def f(length: int, l: list) -> int:
    st_right, right = list(), [-1] * length
    st_left, left = list(), [-1] * length
    st_right.append(0)
    st_left.append(length - 1)

    for i in range(1, length):
        while l[st_right[-1]] > l[i]: right[st_right.pop()] = i
        st_right.append(i)
        while l[st_left[-1]] > l[length - i - 1]: left[st_left.pop()] = length - i - 1
        left.append(length - i - 1)

    return max([l[i] * (abs(right[i] if right[i] > -1 else length - left[i] + 1 if left[i] > -1 else 0 - 1)) for i in range(length)])

data = list(map(int, input().split()))
print(str(f(data[0], data[1:])))
