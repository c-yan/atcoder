from itertools import product

N = int(input())
a = list(map(int, input().split()))

c = {}
for e in a:
    c.setdefault(e, 0)
    c[e] += 1

if len(set(c)) > 3:
    print('No')
    exit()

t = {}
for x, y in product(set(c), repeat=2):
    i = x
    j = y
    t[i] = 1
    if t[i] > c[i]:
        continue
    t.setdefault(j, 0)
    t[j] += 1
    if t[j] > c[j]:
        continue
    for _ in range(N - 2):
        k = i ^ j
        t.setdefault(k, 0)
        t[k] += 1
        c.setdefault(k, 0)
        if t[k] > c[k]:
            j = -1
            break
        i, j = j, k
    if j ^ x == y:
        print('Yes')
        exit()
print('No')
