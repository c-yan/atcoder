N, K, *A = map(int, open(0).read().split())

t = [0] * N
l = 1
p = 300000
for i in range(N):
    if A[i] <= p:
        l = 1
    else:
        l += 1
    p = A[i]
    t[i] = l
print(sum(1 for i in range(N) if t[i] >= K))
