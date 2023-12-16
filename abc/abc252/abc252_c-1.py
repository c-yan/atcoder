from heapq import heappush, heappop

N = int(input())
S = [[int(c) for c in input()] for _ in range(N)]

result = 10 ** 15
for i in range(10):
    q = []
    for j in range(N):
        heappush(q, S[j].index(i))
    used = set()
    while len(q) != 0:
        x = heappop(q)
        if x in used:
            heappush(q, x + 10)
        else:
            used.add(x)
            t = x
    result = min(result, t)
print(result)
