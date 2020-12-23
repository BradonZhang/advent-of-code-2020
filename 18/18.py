from collections import deque

with open('18.txt') as f:
    lines = f.read().splitlines()

ops = {
    '+': lambda x, y: x + y,
    '*': lambda x, y: x * y,
}
total = 0
for line in lines:
    s = deque()
    tokens = list(line.replace(' ', ''))
    for token in tokens:
        if token == '(':
            s.append('(')
        elif token == ')':
            x = s.pop()
            s.pop()
            if len(s) > 0 and s[-1] != '(':
                op = s.pop()
                y = s.pop()
                s.append(ops[op](x, y))
            else:
                s.append(x)
        elif len(s) == 0 or s[-1] not in ops:
            s.append(token if token in ops else int(token))
        else:
            x = int(token)
            op = s.pop()
            y = s.pop()
            s.append(ops[op](x, y))
    total += s[0]
print(total)

total = 0
for line in lines:
    s = deque(['('])
    tokens = list(line.replace(' ', '')) + [')']
    def condense_mul():
        if len(s) == 0:
            return
        while True:
            x = s.pop()
            if len(s) == 0:
                s.append(x)
                return
            elif s[-1] == '*':
                s.pop()
                y = s.pop()
                s.append(x * y)
            else:
                s.append(x)
                return
    def condense_add():
        if len(s) == 0:
            return
        while True:
            x = s.pop()
            if len(s) == 0:
                s.append(x)
                return
            elif s[-1] == '+':
                s.pop()
                y = s.pop()
                s.append(x + y)
            else:
                s.append(x)
                return
    for token in tokens:
        if token == '(':
            s.append('(')
        elif token == ')':
            condense_mul()
            x = s.pop()
            s.pop()
            s.append(x)
            condense_add()
        elif s[-1] == '+':
            x = int(token)
            s.pop()
            y = s.pop()
            s.append(x + y)
        elif len(s) == 0 or s[-1] != '+':
            s.append(token if token in ops else int(token))
    total += s[0]
print(total)
