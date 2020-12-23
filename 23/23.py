from datetime import datetime

t0 = datetime.now()

with open('23.txt') as f:
    order = [int(x) for x in f.read().strip()]

LOW = min(order)
HIGH = max(order)

nodes = {}

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    def pick_up(self):
        next3 = [self.next, self.next.next, self.next.next.next]
        ints = [x.val for x in next3]
        next_val = self.val - 1
        if next_val < LOW:
            next_val = HIGH
        while next_val in ints:
            next_val -= 1
            if next_val < LOW:
                next_val = HIGH
        self.next = next3[-1].next
        next3[-1].next = nodes[next_val].next
        nodes[next_val].next = next3[0]
        return self.next

root = None
prev = None
for x in order:
    nodes[x] = Node(x)
    if prev is None:
        root = nodes[x]
    else:
        prev.next = nodes[x]
    prev = nodes[x]
prev.next = root

curr = root
for i in range(100):
    curr = curr.pick_up()

res = ''
curr = nodes[1].next
while curr != nodes[1]:
    res += str(curr.val)
    curr = curr.next
print(res)

t1 = datetime.now()
print(t1 - t0, 's elapsed')

order2 = list(range(1, 1000001))
order2[:len(order)] = order

LOW = min(order2)
HIGH = max(order2)

t2 = datetime.now()
print(t2 - t0, 's elapsed')

nodes = {}

root = None
prev = None
for x in order2:
    nodes[x] = Node(x)
    if prev is None:
        root = nodes[x]
    else:
        prev.next = nodes[x]
    prev = nodes[x]
prev.next = root

t3 = datetime.now()
print(t3 - t0, 's elapsed')

curr = root
for i in range(10000000):
    curr = curr.pick_up()

print(nodes[1].next.val * nodes[1].next.next.val)

t4 = datetime.now()
print(t4 - t0, 's elapsed')
