from math import prod

with open('13.txt') as f:
    t, ids = f.read().splitlines()
    t = int(t)
    ids = [int(x) if x != 'x' else None for x in ids.split(',')]

def time(t1):
    return (t1 - (t % t1)) % t1

best = t - 1
for idx in ids:
    if idx is None:
        continue
    if time(idx) < time(best):
        best = idx
print(best * time(best))


resmods = [(-i % n, n) for i, n in enumerate(ids) if n is not None]

res_final, mod_final = resmods[0]
for res, mod in resmods[1:]:
    while res_final % mod != res:
        res_final += mod_final
    mod_final *= mod

print(res_final)

# print(congs)
# N = prod(n if b != 0 else 1 for b, n in congs)
# print(N)
# total = 0
# factors = 1
# for b, n in congs:
#     if b == 0:
#         factors *= n
#     else:
#         total += b * inv_mod(b, n) * N // n
# print(factors)
# print((total * factors) % N)
