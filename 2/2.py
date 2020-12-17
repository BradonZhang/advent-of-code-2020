with open('2.txt') as f:
    lines = f.read().splitlines()

total1 = 0
total2 = 0
for line in lines:
    lo = 0
    hi = 0
    i = 0
    letter = ''
    while line[i] != '-':
        lo *= 10
        lo += ord(line[i]) - ord('0')
        i += 1
    i += 1
    while line[i] != ' ':
        hi *= 10
        hi += ord(line[i]) - ord('0')
        i += 1
    i += 1
    letter = line[i]
    i += 3
    if lo <= line[i:].count(letter) <= hi:
        total1 += 1
    n = len(line) - i
    if lo <= 0 or lo > n or hi <= 0 or hi > n:
        continue
    if (line[i + lo - 1] == letter) != (line[i + hi - 1] == letter):
        total2 += 1
print(total1)
print(total2)
