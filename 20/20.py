import numpy as np

with open('20.txt') as f:
    tiles_in = f.read().split('\n\n')

N = round(len(tiles_in) ** 0.5)
R = len(tiles_in[0].splitlines()) - 1
C = len(tiles_in[0].splitlines()[1])

def rstr(s: str):
    return ''.join(reversed(s))

# Key: str, Value: [(tile, rotated)]
sides_map = {}

class Tile:
    def __init__(self, tile_grid):
        head, *grid = tile_grid.splitlines()
        self.num = int(head.split()[1][:-1])
        self.grid = np.array([list(row) for row in grid])
        self.neighbors = []
        sides = [
            ''.join(self.grid[0]),
            ''.join(line[-1] for line in grid),
            ''.join(reversed(self.grid[-1])),
            ''.join(line[0] for line in reversed(grid)),
        ]
        for side in sides:
            sides_map.setdefault(side, [])
            sides_map.setdefault(rstr(side), [])
            sides_map[side].append((self, False))
            sides_map[rstr(side)].append((self, True))
    def strip(self):
        self.grid = self.grid[1:-1, 1:-1]
    def flipx(self):
        self.grid = np.flip(self.grid, 0)
    def flipy(self):
        self.grid = np.flip(self.grid, 1)
    def rotate(self, n=1):
        self.grid = np.rot90(self.grid, n)
    def fit_l(self, other):
        iters = 0
        while np.any(self.grid[:, 0] != other.grid[:, -1]) and iters < 4:
            self.flipx()
            if np.all(self.grid[:, 0] == other.grid[:, -1]):
                return True
            self.flipx()
            self.rotate()
            iters += 1
        return iters < 4
    def fit_u(self, other):
        iters = 0
        while np.any(self.grid[0, :] != other.grid[-1, :]) and iters < 4:
            self.flipy()
            if np.all(self.grid[0, :] == other.grid[-1, :]):
                return True
            self.flipy()
            self.rotate()
            iters += 1
        return iters < 4
    def __str__(self):
        return f'Tile {self.num}\n' + '\n'.join(''.join(row) for row in self.grid)

tiles = [Tile(tile_grid) for tile_grid in tiles_in]

for side, results in sides_map.items():
    if len(results) == 2:
        if results[0][1]:
            continue
        t1 = results[0][0]
        t2 = results[1][0]
        t1.neighbors.append(t2)
        t2.neighbors.append(t1)

# Part 1: count corners (tiles with only two neighbors)
product = 1
for tile in tiles:
    if len(tile.neighbors) == 2:
        product *= tile.num
print(product)

fitted = set()
final = [[None] * N for _ in range(N)]
c0 = None
c1 = None
c2 = None
for tile in tiles:
    if len(tile.neighbors) == 2:
        c0 = final[0][0] = tile
        c1 = final[0][1] = tile.neighbors[0]
        c2 = final[1][0] = tile.neighbors[1]
        fitted.add(c0.num)
        fitted.add(c1.num)
        break

# Orient top-left corner
while not c1.fit_l(c0):
    c0.flipx()
    if c1.fit_l(c0):
        break
    c0.rotate()
if not c2.fit_u(c0):
    c0.flipy()
    c0.rotate(2)
    c1.flipx()
    c2.fit_u(c0)

for j in range(1, N - 1):
    for neighbor in final[0][j].neighbors:
        if neighbor.num in fitted:
            continue
        if len(neighbor.neighbors) < 4:
            final[0][j + 1] = neighbor
            fitted.add(neighbor.num)
            if not neighbor.fit_l(final[0][j]):
                print('oopsx')

for i in range(1, N):
    for j in range(N):
        for neighbor in final[i - 1][j].neighbors:
            if neighbor.num in fitted:
                continue
            final[i][j] = neighbor
            fitted.add(neighbor.num)
            neighbor.fit_u(final[i - 1][j])
            if j:
                neighbor.fit_l(final[i][j - 1])

for tile in tiles:
    tile.strip()
R -= 2
R *= N
C -= 2
C *= N

grid = np.concatenate(
    tuple(np.concatenate(tuple(tile.grid for tile in row), 1) for row in final)
)

monster_txt = """                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """
monster = np.array(
    [np.array(list(line.replace('#', '.'))) for line in monster_txt.splitlines()]
)

MR, MC = monster.shape
num_hash = (grid == '#').sum()
hash_per_monster = monster_txt.count('#')
for rotation in range(4):
    found = False
    for reflection in range(2):
        count = 0
        for i in range(R - MR + 1):
            for j in range(C - MC + 1):
                if np.all(grid[i:i+MR, j:j+MC] != monster):
                    count += 1
        if count:
            found = True
            print(num_hash - hash_per_monster * count)
            break
        grid = np.flip(grid, 0)
    if found:
        break
    grid = np.rot90(grid)
