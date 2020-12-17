with open('16.txt') as f:
    text = f.read()

class Rule:
    def __init__(self, line):
        self.name, bounds_str = line.split(': ')
        bound1_str, bound2_str = bounds_str.split(' or ')
        self.bound1 = tuple(int(x) for x in bound1_str.split('-'))
        self.bound2 = tuple(int(x) for x in bound2_str.split('-'))
    def follows(self, num: int):
        return self.bound1[0] <= num <= self.bound1[1] or self.bound2[0] <= num <= self.bound2[1]

rules_str, ticket_str, lines_str = text.split('\n\n')
ticket = [int(x) for x in ticket_str.splitlines()[-1].split(',')]
_, *lines = lines_str.splitlines()

rules = [Rule(line) for line in rules_str.splitlines()]

ignored = set()
total = 0
for i, line in enumerate(lines):
    fields = (int(x) for x in line.split(','))
    for field in fields:
        followed = False
        for rule in rules:
            if rule.follows(field):
                followed = True
                break
        if not followed:
            total += field
            ignored.add(i)

print(total)

n = len(rules)
poss = [[True] * n for _ in range(n)]
lines = [[int(x) for x in line.split(',')] for i, line in enumerate(lines) if i not in ignored]

for fields in lines:
    followed = False
    for i, field in enumerate(fields):
        for j, rule in enumerate(rules):
            if not poss[i][j]:
                continue
            if not rule.follows(field):
                poss[i][j] = False

# print(' ', '\t', ','.join(chr(x + ord('A')) for x in range(n)))
# for i, line in enumerate(poss):
#     print(i, '\t', ','.join('#' if x else ' ' for x in line))
# print()

alone_count = 0
found = set()
while alone_count < n:
    for r in range(n):
        for c in range(n):
            if not poss[r][c]:
                continue
            if (r, c) in found:
                continue
            alone = True
            for j in range(n):
                if j == c:
                    continue
                if poss[r][j]:
                    alone = False
                    break
            if not alone:
                alone = True
                for j in range(n):
                    if j == c:
                        continue
                    if poss[r][j]:
                        alone = False
                        break
            if alone:
                for i in range(n):
                    if i != r:
                        poss[i][c] = False
                for j in range(n):
                    if j != c:
                        poss[r][j] = False
                alone_count += 1
                found.add((r, c))


# print(' ', '\t', ','.join(chr(x + ord('A')) for x in range(n)))
# for i, line in enumerate(poss):
#     print(i, '\t', ','.join('#' if x else ' ' for x in line))
# print()

field2rule = [poss_field.index(True) for poss_field in poss]
product = 1
for f, r in enumerate(field2rule):
    if rules[r].name.startswith('departure'):
        product *= ticket[f]
print(product)
