with open('21.txt') as f:
    lines = f.read().splitlines()

poss = {}
for line in lines:
    ings_str, allers_str = line[:-1].split(' (contains ')
    ings = ings_str.split()
    allers = allers_str.split(', ')
    for aller in allers:
        poss.setdefault(aller, set(ings))
        poss[aller] &= set(ings)

final = {}
while len(final) != len(poss):
    for aller, ings in poss.items():
        if len(ings) == 1:
            ing = list(ings)[0]
            final[aller] = ing
            for aller, ings in poss.items():
                ings.discard(ing)

total = 0
for line in lines:
    ings_str, allers_str = line[:-1].split(' (contains ')
    ings = ings_str.split()
    for ing in ings:
        if ing not in final.values():
            total += 1

print(total)

final_list = sorted(final.items(), key=lambda x: x[0])
print(','.join(v for k, v in final_list))
