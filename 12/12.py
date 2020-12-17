import math
import numpy as np

with open('12.txt') as f:
    lines = [(line[0], int(line[1:])) for line in f.read().splitlines()]

pos = np.array([0, 0])
order = ['E', 'N', 'W', 'S']
turn = 0
dirs = {
    'N': np.array([0, 1]),
    'S': np.array([0, -1]),
    'E': np.array([1, 0]),
    'W': np.array([-1, 0]),
}

for line in lines:
    cmd, mag = line
    if cmd in order:
        pos += mag * dirs[cmd]
    elif cmd == 'F':
        pos += mag * dirs[order[turn]]
    elif cmd == 'L':
        turn += mag // 90
        turn %= 4
    elif cmd == 'R':
        turn -= mag // 90
        turn %= 4

print(sum(abs(pos)))

pos = np.array([0, 0])
way = np.array([10, 1])
dirs = {
    'N': np.array([0, 1]),
    'S': np.array([0, -1]),
    'E': np.array([1, 0]),
    'W': np.array([-1, 0]),
}

l_mat = np.array([[0, -1], [1, 0]])
rots = [l_mat ** i for i in range(4)]

for line in lines:
    cmd, mag = line
    if cmd in order:
        way += mag * dirs[cmd]
    elif cmd == 'F':
        pos += mag * way
    elif cmd == 'L':
        for i in range(mag // 90):
            way = np.flip(way)
            way *= np.array([-1, 1])
        # way = rots[mag // 90] @ way
    elif cmd == 'R':
        for i in range(4 - mag // 90):
            way = np.flip(way)
            way *= np.array([-1, 1])
        # way = way @ rots[mag // 90]

print(sum(abs(pos)))
