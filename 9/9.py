from collections import deque

with open('9.txt') as f:
    nums = [int(line) for line in f.read().splitlines()]

weak = None
q = deque(nums[:25], maxlen=25)
for num in nums[25:]:
    valid = False
    for x in q:
        if valid:
            break
        for y in q:
            if x + y == num:
                valid = True
                break
    if not valid:
        weak = num
        break
    q.append(num)

print(weak)

accum = 0
sums = [0]
n = len(nums)
for num in nums:
    accum += num
    sums.append(accum)
for i in range(n + 1):
    for j in range(i, n + 1):
        if j - i < 2:
            continue
        if sums[j] - sums[i] == weak:
            sub = nums[i:j]
            print(max(sub) + min(sub))
