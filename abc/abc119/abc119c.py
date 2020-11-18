from itertools import product

N, A, B, C, *l = map(int, open(0).read().split())

result = float('inf')
for p in product(range(4), repeat=N):
    c = [0, 0, 0, 0]
    v = [0, 0, 0, 0]
    for i in range(N):
        c[p[i]] += 1
        v[p[i]] += l[i]
    if min(c[:3]) == 0:
        continue
    t = abs(A - v[0]) + abs(B - v[1]) + abs(C - v[2]) + (sum(c[:3]) - 3) * 10
    result = min(result, t)
print(result)
