from sys import stdin

readline = stdin.readline

N, X = map(int, readline().split())
t = set([0])
for _ in range(N):
    a, b = map(int, readline().split())
    u = set()
    for x in t:
        u.add(x + a)
        u.add(x + b)
    t = u

if X in t:
    print('Yes')
else:
    print('No')
