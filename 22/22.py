from collections import deque

with open('22.txt') as f:
    p1, p2 = [deque([int(x) for x in body.splitlines()[1:]]) for body in f.read().split('\n\n')]

while len(p1) and len(p2):
    c1 = p1.popleft()
    c2 = p2.popleft()
    if c1 > c2:
        p1.append(c1)
        p1.append(c2)
    else:
        p2.append(c2)
        p2.append(c1)

winner = p1 if len(p1) else p2
mult = 1
total = 0
while len(winner):
    total += winner.pop() * mult
    mult += 1
print(total)

with open('22.txt') as f:
    p1, p2 = [deque([int(x) for x in body.splitlines()[1:]]) for body in f.read().split('\n\n')]

depth = 1
mem = {}
def game(p1, p2):
    global depth
    seen = set()
    while len(p1) and len(p2):
        k = (tuple(p1), tuple(p2))
        if k in seen:
            depth -= 1
            mem.update(dict.fromkeys(seen, True))
            return True
        seen.add(k)
        c1 = p1.popleft()
        c2 = p2.popleft()
        p1won = c1 > c2
        if c1 <= len(p1) and c2 <= len(p2):
            depth += 1
            p1won = game(deque(list(p1)[:c1]), deque(list(p2)[:c2]))
        if p1won:
            p1.append(c1)
            p1.append(c2)
        else:
            p2.append(c2)
            p2.append(c1)
    depth -= 1
    res = bool(len(p1))
    mem.update(dict.fromkeys(seen, res))
    if not depth:
        winner = p1 if len(p1) else p2
        mult = 1
        total = 0
        while len(winner):
            total += winner.pop() * mult
            mult += 1
        print(total)
    return res

game(p1, p2)
