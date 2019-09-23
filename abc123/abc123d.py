from heapq import heappush, heappop

X, Y, Z, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)

exists = set()
q = [(-(A[0] + B[0] + C[0]), (0, 0, 0))]
for _ in range(K):
    v, i = heappop(q)
    print(-v)
    if i[0] < X - 1:
        ni = (i[0] + 1, i[1], i[2])
        if ni not in exists:
            exists.add(ni)
            nv = A[i[0] + 1] + B[i[1]] + C[i[2]]
            heappush(q, (-nv, ni))
    if i[1] < Y - 1:
        ni = (i[0], i[1] + 1, i[2])
        if ni not in exists:
            exists.add(ni)
            nv = A[i[0]] + B[i[1] + 1] + C[i[2]]
            heappush(q, (-nv, ni))
    if i[2] < Z - 1:
        ni = (i[0], i[1], i[2] + 1)
        if ni not in exists:
            exists.add(ni)
            nv = A[i[0]] + B[i[1]] + C[i[2] + 1]
            heappush(q, (-nv, ni))
