with open('10.txt') as f:
    nums = [int(x) for x in f.read().splitlines()]

nums.sort()
last = 0
d1 = 0
d3 = 0
for num in nums:
    if num - last == 1:
        d1 += 1
    elif num - last == 3:
        d3 += 1
    last = num
d3 += 1
print(d1 * d3)

n = len(nums)
counts = [0] * n + [1]
for i in range(n - 1, -1, -1):
    val = nums[i - 1] if i else 0
    for j in range(i + 1, i + 4):
        if j > n:
            break
        if nums[j - 1] - val <= 3:
            counts[i] += counts[j]

print(counts[0])
