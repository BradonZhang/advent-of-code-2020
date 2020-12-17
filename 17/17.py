with open('17.txt') as f:
    initial = f.read().splitlines()

cubes = set()
for i, r in enumerate(initial):
    for j, c in enumerate(r):
        if c == '#':
            cubes.add((i, j, 0))

cycle = 0
while cycle < 6:
    new_cubes = set(cubes)
    marked = {}
    for x, y, z in cubes:
        neighbors = 0
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                for dz in range(-1, 2):
                    if dx == 0 and dy == 0 and dz == 0:
                        continue
                    cube = (x + dx, y + dy, z + dz)
                    if cube in cubes:
                        neighbors += 1
                    else:
                        if cube not in marked:
                            marked[cube] = 0
                        marked[cube] += 1
        if neighbors not in [2, 3]:
            new_cubes.discard((x, y, z))
    for cube, count in marked.items():
        if count == 3:
            new_cubes.add(cube)
    cubes = new_cubes
    cycle += 1
print(len(cubes))


cubes = set()
for i, r in enumerate(initial):
    for j, c in enumerate(r):
        if c == '#':
            cubes.add((i, j, 0, 0))

cycle = 0
while cycle < 6:
    new_cubes = set(cubes)
    marked = {}
    for x, y, z, w in cubes:
        neighbors = 0
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                for dz in range(-1, 2):
                    for dw in range(-1, 2):
                        if dx == 0 and dy == 0 and dz == 0 and dw == 0:
                            continue
                        cube = (x + dx, y + dy, z + dz, w + dw)
                        if cube in cubes:
                            neighbors += 1
                        else:
                            if cube not in marked:
                                marked[cube] = 0
                            marked[cube] += 1
        if neighbors not in [2, 3]:
            new_cubes.discard((x, y, z, w))
    for cube, count in marked.items():
        if count == 3:
            new_cubes.add(cube)
    cubes = new_cubes
    cycle += 1
print(len(cubes))
