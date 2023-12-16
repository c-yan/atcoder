N, K = map(int, input().split())
A = [int(a) - 1 for a in input().split()]

if K <= N:
    p = 0
    for i in range(K):
        p = A[p]
    print(p + 1)
    exit()

p = 0
t = [-1] * N
t[0] = 0
for i in range(1, N):
    p = A[p]
    if t[p] != -1:
        break
    t[p] = i

d = i - t[p]
K -= i
K %= d

for i in range(K):
    p = A[p]
print(p + 1)
