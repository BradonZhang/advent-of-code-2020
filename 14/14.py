with open('14.txt') as f:
    lines = f.read().splitlines()

mem = {}
mask_and = ~0
mask_or = 0
for line in lines:
    if line.startswith('mask'):
        mask = line.split()[-1]
        mask_and = int(mask.replace('X', '1'), 2)
        mask_or = int(mask.replace('X', '0'), 2)
    else:
        key = int(line[4:].split(']')[0])
        val = int(line.split()[-1])
        mem[key] = (val & mask_and) | mask_or
print(sum(v for k, v in mem.items()))

mem = {}
mask_or = 0
mask_float = 0
floaters = []
for line in lines:
    if line.startswith('mask'):
        mask = line.split()[-1]
        mask_or = int(mask.replace('X', '0'), 2)
        mask_float = int(mask.replace('1', '0').replace('X', '1'), 2)
        floaters = []
        for i in range(36):
            bit = (mask_float >> i) & 1
            if bit:
                floaters.append(1 << i)
    else:
        key = int(line[4:].split(']')[0])
        val = int(line.split()[-1])
        keys = [(key | mask_or) & ~mask_float]
        for floater in floaters:
            n = len(keys)
            keys *= 2
            for i in range(n):
                keys[i] |= floater
        for key in keys:
            mem[key] = val
print(sum(v for k, v in mem.items()))
