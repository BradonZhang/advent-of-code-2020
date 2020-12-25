with open('24.txt') as f:
    lines = [line.replace('ne', 'd').replace('se', 'f').replace('nw', 'v').replace('sw', 'x') for line in f.read().splitlines()]

def norm(cell):
    d, w, f = cell
    if d < 0:
        w -= d
        f -= d
        d = 0
    if w < 0:
        d -= w
        f -= w
        w = 0
    if f < 0:
        d -= f
        w -= f
        f = 0
    m = min(d, w, f)
    d -= m
    w -= m
    f -= m
    return (d, w, f)

flipped = set()
for line in lines:
    d = 0
    w = 0
    f = 0
    for c in line:
        if c == 'd':
            d += 1
        elif c == 'w':
            w += 1
        elif c == 'f':
            f += 1
        elif c == 'x':
            d -= 1
        elif c == 'e':
            w -= 1
        elif c == 'v':
            f -= 1
    cell = norm((d, w, f))
    if cell in flipped:
        flipped.discard(cell)
    else:
        flipped.add(cell)
print(len(flipped))

T = 100
neighbors = [
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (-1, 0, 0),
    (0, -1, 0),
    (0, 0, -1),
]
for t in range(T):
    blk_adj = dict.fromkeys(flipped, 0)
    wht_adj = {}
    for cell in flipped:
        d, w, f = cell
        for neighbor in neighbors:
            dd, dw, df = neighbor
            new_cell = norm((d + dd, w + dw, f + df))
            if new_cell in flipped:
                blk_adj[new_cell] += 1
            else:
                wht_adj.setdefault(new_cell, 0)
                wht_adj[new_cell] += 1
    for cell, count in blk_adj.items():
        if count == 0 or count > 2:
            flipped.discard(cell)
    for cell, count in wht_adj.items():
        if count == 2:
            flipped.add(cell)
print(len(flipped))
