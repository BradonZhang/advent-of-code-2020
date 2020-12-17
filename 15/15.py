from collections import deque

with open('15.txt') as f:
    nums = [int(x) for x in f.read().strip().split(',')]

mem = {}

def say(index, num):
    if num not in mem:
        mem[num] = deque([], maxlen=2)
    mem[num].append(index)
    return mem[num][1] - mem[num][0] if len(mem[num]) == 2 else 0

next_num = 0
for i, num in enumerate(nums):
    next_num = say(i, num)
for i in range(len(nums), 2019):
    next_num = say(i, next_num)

print(next_num)

for i in range(2019, 30000000 - 1):
    next_num = say(i, next_num)
    
print(next_num)
