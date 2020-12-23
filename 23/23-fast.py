with open('23.txt') as f:
    order = [int(x) for x in f.read().strip()]

N = len(order)
T = 100
nex = [0] * (N + 1)
for i, num in enumerate(order):
    nex[order[i - 1]] = num

curr = order[0]
for t in range(T):
    hand = (nex[curr], nex[nex[curr]], nex[nex[nex[curr]]])
    nex[curr] = nex[hand[-1]]
    j = curr - 1 if curr > 1 else N
    while j in hand:
        j = (j - 2) % N + 1
    nex[hand[-1]] = nex[j]
    nex[j] = hand[0]
    curr = nex[curr]

res = 0
curr = nex[1]
while curr != 1:
    res = (res * 10) + curr
    curr = nex[curr]
print(res)

N = 1000000
T = 10000000
nex = list(range(1, N + 2))
nex[0] = 0
for i, num in enumerate(order):
    nex[order[i - 1]] = num
nex[order[-1]] = len(order) + 1
nex[-1] = order[0]

curr = order[0]
for t in range(T):
    hand = (nex[curr], nex[nex[curr]], nex[nex[nex[curr]]])
    nex[curr] = nex[hand[-1]]
    j = curr - 1 if curr > 1 else N
    while j in hand:
        j = (j - 2) % N + 1
    nex[hand[-1]] = nex[j]
    nex[j] = hand[0]
    curr = nex[curr]

print(nex[1] * nex[nex[1]])
