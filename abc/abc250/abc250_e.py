from sys import stdin
from random import sample

readline = stdin.readline

N = int(readline())
a = list(map(int, readline().split()))
b = list(map(int, readline().split()))

v = set(a + b)
d = {}
for x, y in zip(v, sample(range(10 ** 18), len(v))) :
    d[x] = y

def hash(xs):
    result = []
    appeared = set()
    h = 0
    for x in xs:
        if x not in appeared:
            appeared.add(x)
            h ^= x
        result.append(h)
    return result

ha = hash(d[x] for x in a)
hb = hash(d[x] for x in b)

Q = int(readline())
result = []
for _ in range(Q):
    x, y = map(int, readline().split())
    if ha[x - 1] == hb[y - 1]:
        result.append('Yes')
    else:
        result.append('No')
print(*result, sep='\n')
