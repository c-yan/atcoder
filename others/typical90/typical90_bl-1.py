from sys import stdin

readline = stdin.readline

N, Q = map(int, readline().split())
A = list(map(int, readline().split()))

d = [A[i] - A[i + 1] for i in range(N - 1)]

t = sum(abs(x) for x in d)
result = []
for _ in range(Q):
    L, R, V = map(int, readline().split())
    L, R = L - 1, R - 1
    if L != 0:
        t -= abs(d[L - 1])
        d[L - 1] -= V
        t += abs(d[L - 1])
    if R != N - 1:
        t -= abs(d[R])
        d[R] += V
        t += abs(d[R])
    result.append(t)
print(*result, sep='\n')
