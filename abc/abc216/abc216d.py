from sys import stdin
from collections import deque

readline = stdin.readline

N, M = map(int, readline().split())
a = [None] * M
for i in range(M):
    k = int(readline())
    a[i] = deque(map(int, readline().split()))

q = deque(range(M))
t = {}
while q:
    i = q.popleft()
    if len(a[i]) == 0:
        continue
    x = a[i].popleft()
    if x not in t:
        t[x] = i
        continue
    q.append(i)
    q.append(t[x])
    del t[x]

if all(len(d) == 0 for d in a):
    print('Yes')
else:
    print('No')
