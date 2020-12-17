from math import prod

with open('1.txt') as f:
    nums = [int(x) for x in f.read().splitlines()]
    comps = [2020 - x for x in nums]

print(prod(set(nums) & set(comps)))

pairs = {}
for x in nums:
    for y in nums:
        pairs[2020 - (x + y)] = (x, y)
for x in nums:
    if x in pairs:
        print(prod(pairs[x]) * x)
        break
