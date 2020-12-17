class Rule:
    def __init__(self, line):
        tokens = line.split()
        self.fr = (tokens[0], tokens[1])
        contents = ' '.join(tokens[4:]).split(',')
        self.to = {}
        for content in contents:
            tokens = content.split()
            if tokens[0] == 'no':
                break
            count = int(tokens[0])
            key = (tokens[1], tokens[2])
            self.to[key] = count

with open('7.txt') as f:
    rules = [Rule(line) for line in f.read().splitlines()]

rule_map = {}
for rule in rules:
    rule_map[rule.fr] = rule

res = {}
def visit(desc):
    if desc in res:
        return res[desc]
    res[desc] = False
    for to_desc in rule_map[desc].to:
        if to_desc == ('shiny', 'gold'):
            res[desc] = True
        else:
            res[desc] = res[desc] or visit(to_desc)
    return res[desc]
    
total = 0
for rule in rules:
    if visit(rule.fr):
        total += 1
print(total)

res = {}
def visit2(desc):
    if desc in res:
        return res[desc]
    total = 0
    for to_desc, count in rule_map[desc].to.items():
        total += count + count * visit2(to_desc)
    res[desc] = total
    return total
    
total = 0
for rule in rules:
    total += visit2(rule.fr)
print(visit2(('shiny', 'gold')))
