N, M, D, *A = map(int, open(0).read().split())

def synthesize(a, b):
    result = list(a)
    for i in range(N):
        result[i] = b[a[i]]
    return tuple(result)

u = list(range(N))
for a in A:
    u[a - 1], u[a] = u[a], u[a - 1]
u = tuple(u)

d = D
t = tuple(range(N))
while d != 0:
    if d & 1 == 1:
        t = synthesize(t, u)
    u = synthesize(u, u)
    d >>= 1
result = [0] * N
for i in range(N):
    result[t[i]] = i + 1
print(*result, sep='\n')
