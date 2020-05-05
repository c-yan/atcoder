from heapq import heappush, heappop

N, K, D = map(int, input().split())
A = list(map(int, input().split()))

if 1 + (K - 1) * D > N:
    print(-1)
    exit()

result = []
q = []
i = 0
l = 0
for k in range(K - 1, -1, -1):
    for j in range(l, N - k * D):
        heappush(q, (A[j], j))
    l = N - k * D
    while True:
        a, j = heappop(q)
        if j >= i:
            break
    result.append(a)
    i = j + D
print(*result)
