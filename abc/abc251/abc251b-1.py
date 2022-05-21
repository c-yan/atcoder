from itertools import combinations

N, W, *A = map(int, open(0).read().split())

a = [x for x in A if x <= W]
s = set(a)

for x, y in combinations(A, 2):
    v = x + y
    if v > W:
        continue
    s.add(v)

for x, y, z in combinations(A, 3):
    v = x + y + z
    if v > W:
        continue
    s.add(v)

print(len(s))
