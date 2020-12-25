with open('19.txt') as f:
    rules_str, queries = (x.splitlines() for x in f.read().split('\n\n'))

class Rule:
    def __init__(self, rule_str):
        self.letter = rule_str[1:-1] if rule_str[0] == '"' else None
        self.deps = []
        if self.letter is None:
            sections = rule_str.split(' | ')
            for section in sections:
                self.deps.append([int(x) for x in section.split()])
    def match(self, query):
        if self.letter is not None:
            return set((len(self.letter),)) if query.startswith(self.letter) else set()
        matches = set()
        for group in self.deps:
            group_matches = set((0,))
            for rule_num in group:
                rule_matches = set()
                for match in group_matches:
                    temp_matches = rules[rule_num].match(query[match:])
                    for temp_match in temp_matches:
                        rule_matches.add(match + temp_match)
                group_matches = rule_matches
            matches |= group_matches
        return matches

rules = dict([(int(line.split(': ')[0]), Rule(line.split(': ')[1])) for line in rules_str])

print(sum(1 if len(query) in rules[0].match(query) else 0 for query in queries))

rules[8] = Rule('42 | 42 8')
rules[11] = Rule('42 31 | 42 11 31')

print(sum(1 if len(query) in rules[0].match(query) else 0 for query in queries))
