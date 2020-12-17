with open('6.txt') as f:
    groups = [group.splitlines() for group in f.read().split('\n\n')]

total = 0
for group in groups:
    answered = set()
    for person in group:
        answered |= set(person)
    total += len(answered)
print(total)

total = 0
for group in groups:
    answered = set(group[0])
    for person in group:
        answered &= set(person)
    total += len(answered)
print(total)
