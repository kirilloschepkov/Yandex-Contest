length, max_cnt = map(int, input().split())
line = input()
counts = [0] * 26
left = right = basic_left = basic_right = 0
while right < length:
    if counts[ord(line[right]) - ord('a')] < max_cnt:
        if right - left > basic_right - basic_left: basic_right, basic_left = right, left
        counts[ord(line[right]) - ord('a')] += 1
        right += 1
    else:
        left = right - max_cnt + 1
        counts = [0] * 26
print(basic_right - basic_left + 1, basic_left + 1)
