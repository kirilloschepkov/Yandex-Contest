input()
shirts = list(map(int, input().split()))
input()
pants = list(map(int, input().split()))
i_shirts = i_pants = 0
best = 10**6
answer = None

while i_shirts < len(shirts) and i_pants < len(pants):
    now = abs(shirts[i_shirts] - pants[i_pants])
    if now < best:
        best = now
        answer = (shirts[i_shirts], pants[i_pants])
    if shirts[i_shirts] > pants[i_pants]: i_pants += 1
    else: i_shirts += 1

print(' '.join(map(str, answer)))
