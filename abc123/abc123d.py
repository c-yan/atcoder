from heapq import heappush, heappop

X, Y, Z, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

for l in [A, B, C]:
    l.sort()

exists = set()
q = [(-(A[X - 1] + B[Y - 1] + C[Z - 1]), (X - 1, Y - 1, Z - 1))]
for _ in range(K):
    v, n = heappop(q)
    print(-v)
    for i in range(3):
        if n[i] > 0:
            t = [n[j] for j in range(3)]
            t[i] -= 1
            nn = tuple(t)
            if nn not in exists:
                exists.add(nn)
                nv = A[nn[0]] + B[nn[1]] + C[nn[2]]
                heappush(q, (-nv, nn))
