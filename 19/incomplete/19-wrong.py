import functools

with open('19.txt') as f:
    rules_str, queries_str = f.read().split('\n\n')

rules = {}
part2 = False

def eval_rule(x, nums1, nums2=None):
    curr = x
    for num in nums1:
        curr = rules[num].func(curr)
        if curr is None:
            break
    if curr is not None or nums2 is None:
        return curr
    curr = x
    # elif part2 and num == 8:
    #     print(8)
    for num in nums2:
        if part2 and num == 11:
            # curr = rules[42].func(curr)
            # if curr is None:
            #     return None
            n = len(curr)
            for i in range(-1, -n - 1, -1):
                if rules[31].func(curr[i:]) == '':
                    return rules[11].func(curr[:i])
            print('oof')
            return None
        curr = rules[num].func(curr)
        if curr is None:
            break
    return curr

class Rule:
    def __init__(self, line):
        rule_num, rest = line.split(': ')
        self.num = int(rule_num)
        if rest[0] == '"':
            self.func = lambda x: x[1:] if x is not None and x.startswith(rest[1]) else None
        else:
            ors = rest.split(' | ')
            if len(ors) == 2:
                n1 = [int(x) for x in ors[0].split()]
                n2 = [int(x) for x in ors[1].split()]
                self.func = lambda x: eval_rule(x, n1, n2)
            elif len(ors) == 1:
                n1 = [int(x) for x in ors[0].split()]
                self.func = lambda x: eval_rule(x, n1)
        rules[self.num] = self

for x in rules_str.splitlines():
    _ = Rule(x)

queries = queries_str.splitlines()
total = 0
for query in queries:
    if rules[0].func(query) == '':
        total += 1
print(total)

part2 = True
Rule("8: 42 | 42 8")
Rule("11: 42 31 | 42 11 31")

total = 0
for i, query in enumerate(queries):
    if rules[0].func(query) == '':
        total += 1
print(total)
