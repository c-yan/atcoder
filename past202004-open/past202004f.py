from heapq import heappush, heappop

N = int(input())

d = {}
for _ in range(N):
    A, B = map(int, input().split())
    d.setdefault(A, [])
    d[A].append(B)

t = []
result = 0
for i in range(1, N + 1):
    if i in d:
        for b in d[i]:
            heappush(t, -b)
    result += -heappop(t)
    print(result)
