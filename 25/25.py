with open('25.txt') as f:
    pkey1, pkey2 = (int(x) for x in f.read().splitlines())

SUBJ = 7
MOD = 20201227
iter = lambda x, subj: (x * subj) % MOD

x = 1
l1 = 0
while x != pkey1:
    l1 += 1
    x = iter(x, SUBJ)

x = 1
l2 = 0
while x != pkey2:
    l2 += 1
    x = iter(x, SUBJ)

x = 1
for i in range(l1):
    x = iter(x, pkey2)
print(x)

x = 1
for i in range(l2):
    x = iter(x, pkey1)
print(x)
