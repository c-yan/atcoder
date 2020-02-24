w = input()

d = {}
for c in w:
    if c in d:
        d[c] += 1
    else:
        d[c] = 1

if all(v % 2 == 0 for v in d.values()):
    print('Yes')
else:
    print('No')
