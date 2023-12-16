from sys import stdin
from collections import deque

readline = stdin.readline

Q = int(readline())

q = deque([])
result = []
for _ in range(Q):
    t, x = map(int, readline().split())
    if t == 1:
        q.appendleft(x)
    elif t == 2:
        q.append(x)
    elif t == 3:
        result.append(q[x - 1])
print(*result, sep='\n')
