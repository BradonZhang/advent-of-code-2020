with open('3.txt') as f:
    trees = f.read().splitlines()

num_trees = 0
n = len(trees[0])
m = len(trees)
for i in range(m):
    if trees[i][(3 * i) % n] == '#':
        num_trees += 1
print(num_trees)

num_trees = 0
slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
prod = 1
for r, c in slopes:
    for i in range(0, m, r):
        if trees[i][(c * i // r) % n] == '#':
            num_trees += 1
    prod *= num_trees
    num_trees = 0
print(prod)
