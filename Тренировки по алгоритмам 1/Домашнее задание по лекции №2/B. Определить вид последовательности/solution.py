def f(n: list) -> str:
    answer = ''
    for i in range(1, len(n)):
        if n[i - 1] < n[i]:
            if answer == 'DESCENDING' or answer == 'WEAKLY DESCENDING': return 'RANDOM'
            elif answer == 'CONSTANT' or answer == 'WEAKLY ASCENDING': answer = 'WEAKLY ASCENDING'
            else: answer = 'ASCENDING'
        elif n[i - 1] > n[i]:
            if answer == 'ASCENDING' or answer == 'WEAKLY ASCENDING': return 'RANDOM'
            elif answer == 'CONSTANT' or answer == 'WEAKLY DESCENDING': answer = 'WEAKLY DESCENDING'
            else: answer = 'DESCENDING'
        else:
            if answer == 'DESCENDING': answer = 'WEAKLY DESCENDING'
            elif answer == 'ASCENDING': answer = 'WEAKLY ASCENDING'
            elif answer == '': answer = 'CONSTANT'
    return answer


nums = list()
while True:
    num = int(input())
    if num == -2*10**9: break
    nums.append(num)

print(f(nums))
