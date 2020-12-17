with open('5.txt') as f:
    lines = f.read().splitlines()
    nums = [line.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1') for line in lines]
    ints = [int(num, 2) for num in nums]

print(max(ints))
ints.sort()
prev = None
for x in ints:
    if prev is not None:
        if x != prev + 1:
            print(x - 1)
            break
    prev = x
