from collections import deque
from sys import stdin

readline = stdin.readline

Q = int(readline())

result = []
q = deque([])
for _ in range(Q):
    query = readline()
    if query[0] == '1':
        _, x, c = map(int, query.split())
        q.append((x, c))
    if query[0] == '2':
        _, c = map(int, query.split())
        r = c
        t = 0
        while True:
            x, c = q.popleft()
            y = min(r, c)
            t += x * y
            r -= y
            c -= y
            if r == 0:
                if c != 0:
                    q.appendleft((x, c))
                break
        result.append(t)
if len(result) != 0:
    print(*result, sep='\n')
