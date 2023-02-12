n, target = list(map(int, input().split()))
nums = list(map(int, input().split()))
left = right = 0
summ = count = 0

while right < n or summ > target:
    if summ < target:
        summ += nums[right]
        right += 1
    elif summ > target:
        summ -= nums[left]
        left += 1
    else:
        count += 1
        summ -= nums[left]
        left += 1
        summ += nums[right]
        right += 1

if summ == target: count += 1
print(count)
