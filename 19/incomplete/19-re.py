import re

with open('19.txt') as f:
    rules_str, queries = (x.splitlines() for x in f.read().split('\n\n'))

class Rule:
    def __init__(self, rule_str):
        self.re = re.compile(rule_str[1:-1]) if rule_str[0] == '"' else None
        self.deps = []
        if self.re is None:
            sections = rule_str.split(' | ')
            for section in sections:
                self.deps.append([int(x) for x in section.split()])
    def get_pattern(self):
        if self.re is None:
            self.compile_re()
        return self.re.pattern
    def match(self, query):
        if self.re is None:
            self.compile_re()
        return self.re.fullmatch(query) is not None
    def compile_re(self):
        if self.re is not None:
            return
        pattern = '|'.join(''.join(rules[num].get_pattern() for num in group)for group in self.deps)
        self.re = re.compile(f'({pattern})')

rules = dict([(int(line.split(': ')[0]), Rule(line.split(': ')[1])) for line in rules_str])

print(sum(1 if rules[0].match(query) else 0 for query in queries))
