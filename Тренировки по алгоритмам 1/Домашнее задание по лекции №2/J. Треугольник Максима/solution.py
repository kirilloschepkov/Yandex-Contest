def f(prev_freq: int, n: list) -> tuple:
    left, right = 30, 4000
    for freq, diff in n:
        freq = float(freq)
        if abs(freq - prev_freq) < 10**(-6): continue
        if diff == 'closer':
            if freq > prev_freq: left = max(left, (freq + prev_freq) / 2)
            else: right = min(right, (freq + prev_freq) / 2)
        elif diff == 'further':
            if freq < prev_freq: left = max(left, (freq + prev_freq) / 2)
            else: right = min(right, (freq + prev_freq) / 2)
        prev_freq = freq
    return left, right


cnt = int(input())
prev = float(input())
notes = [input().split() for _ in range(cnt - 1)]
print(*f(prev, notes))
