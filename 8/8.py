with open('8.txt') as f:
    lines = [(line.split()[0], int(line.split()[1])) for line in f.read().splitlines()]
n = len(lines)

i = 0
visited = set()
acc = 0
while i not in visited:
    visited.add(i)
    ins, x = lines[i]
    if ins == 'jmp':
        i += x - 1
    elif ins == 'acc':
        acc += x
    i += 1
print(acc)

def simul(j):
    L = [line for line in lines]
    ins, x = L[j]
    if ins == 'acc':
        return None
    if ins == 'jmp':
        L[j] = ('nop', x)
    elif ins == 'nop':
        L[j] = ('jmp', x)
    i = 0
    visited = set()
    acc = 0
    while i not in visited and i < n:
        visited.add(i)
        ins, x = L[i]
        if ins == 'jmp':
            i += x - 1
        elif ins == 'acc':
            acc += x
        i += 1
    if i >= n:
        print(acc)

for i in range(n):
    simul(i)
