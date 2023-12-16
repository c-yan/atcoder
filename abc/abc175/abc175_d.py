N, K = map(int, input().split())
P = list(map(int, input().split()))
C = list(map(int, input().split()))

result = -float('inf')
for i in range(N):
    p = P[i] - 1
    c = C[p]
    k = K - 1
    t = c
    while p != i and k != 0:
        p = P[p] - 1
        c += C[p]
        t = max(t, c)
        k -= 1
    if k == 0 or c <= 0:
        result = max(result, t)
        continue
    l = K - k
    c = c * (K // l - 1)
    k = K - (K // l - 1) * l
    t = c
    while k != 0:
        p = P[p] - 1
        c += C[p]
        t = max(t, c)
        k -= 1
    result = max(result, t)
print(result)
