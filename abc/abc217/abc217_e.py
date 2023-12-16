from sys import stdin
from collections import deque
from heapq import heappop, heappush

readline = stdin.readline

Q = int(readline())

h = []
d = deque([])
result = []
for _ in range(Q):
    query = readline()
    if query[0] == '1':
        _, x = map(int, query.split())
        d.append(x)
    elif query[0] == '2':
        if len(h) == 0:
            result.append(d.popleft())
        else:
            result.append(heappop(h))
    elif query[0] == '3':
        for x in d:
            heappush(h, x)
        d = deque([])
print(*result, sep='\n')
