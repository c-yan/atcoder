N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

fac = [0] * 8
fac[1] = 1
for i in range(2, N):
    fac[i] = i * fac[i - 1]

a = 0
l = list(range(1, N + 1))
for i in range(N):
    a += l.index(P[i]) * fac[len(l) - 1]
    l.remove(P[i])

b = 0
l = list(range(1, N + 1))
for i in range(N):
    b += l.index(Q[i]) * fac[len(l) - 1]
    l.remove(Q[i])

print(abs(a - b))
