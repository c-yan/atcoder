from sys import stdin
from heapq import heappop, heappush

readline = stdin.readline

Q = int(readline())
t = 0
result = []
bag = []
for _ in range(Q):
    query = readline()
    if query[0] == '1':
        _, X = map(int, query.split())
        heappush(bag, X - t)
    elif query[0] == '2':
        _, X = map(int, query.split())
        t += X
    elif query[0] == '3':
        result.append(heappop(bag) + t)
print(*result, sep='\n')
