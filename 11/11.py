from copy import deepcopy

with open('11.txt') as f:
    orig_grid = [list(line) for line in f.read().splitlines()]

grid = deepcopy(orig_grid)
R = len(grid)
C = len(grid[0])

def can_fill(row, col):
    if grid[row][col] == '#':
        return False
    for i in range(row - 1, row + 2):
        if i < 0 or i >= R:
            continue
        for j in range(col - 1, col + 2):
            if j < 0 or j >= C or (i == row and j == col):
                continue
            if grid[i][j] == '#':
                return False
    return True

def can_empty(row, col):
    if grid[row][col] == 'L':
        return False
    rem = 4
    for i in range(row - 1, row + 2):
        if i < 0 or i >= R:
            continue
        for j in range(col - 1, col + 2):
            if j < 0 or j >= C or (i == row and j == col):
                continue
            if grid[i][j] == '#':
                rem -= 1
                if rem == 0:
                    return True
    return False

changed = True
while changed:
    changed = False
    grid_copy = deepcopy(grid)
    for i in range(R):
        for j in range(C):
            if grid[i][j] == '.':
                continue
            if can_empty(i, j):
                changed = True
                grid_copy[i][j] = 'L'
            elif can_fill(i, j):
                changed = True
                grid_copy[i][j] = '#'
    grid = grid_copy

print(sum(sum(int(x == '#') for x in row) for row in grid))

grid = deepcopy(orig_grid)

def can_fill2(row, col):
    if grid[row][col] != 'L':
        return False
    for dr in range(-1, 2):
        i = row + dr
        if i < 0 or i >= R:
            continue
        for dc in range(-1, 2):
            i = row + dr
            j = col + dc
            if j < 0 or j >= C or (dr == 0 and dc == 0):
                continue
            while 0 <= i < R and 0 <= j < C:
                if grid[i][j] == '#':
                    return False
                elif grid[i][j] == 'L':
                    break
                i += dr
                j += dc
    return True

def can_empty2(row, col):
    if grid[row][col] != '#':
        return False
    rem = 5
    for dr in range(-1, 2):
        i = row + dr
        if i < 0 or i >= R:
            continue
        for dc in range(-1, 2):
            i = row + dr
            j = col + dc
            if j < 0 or j >= C or (dr == 0 and dc == 0):
                continue
            while 0 <= i < R and 0 <= j < C:
                if grid[i][j] == '#':
                    rem -= 1
                    if rem == 0:
                        return True
                    break
                elif grid[i][j] == 'L':
                    break
                i += dr
                j += dc
    return False

changed = True
while changed:
    changed = False
    grid_copy = deepcopy(grid)
    for i in range(R):
        for j in range(C):
            if grid[i][j] == '.':
                continue
            if can_empty2(i, j):
                changed = True
                grid_copy[i][j] = 'L'
            elif can_fill2(i, j):
                changed = True
                grid_copy[i][j] = '#'
    grid = grid_copy

print(sum(sum(int(x == '#') for x in row) for row in grid))
