# 累積和(gcd)
from fractions import gcd

N = int(input())
A = list(map(int, input().split()))

lcg = A[:]
rcg = A[:]
for i in range(1, N):
    lcg[i] = gcd(lcg[i], lcg[i - 1])
for i in range(N - 2, -1, -1):
    rcg[i] = gcd(rcg[i], rcg[i + 1])

t = [0] * N
t[0] = rcg[1]
for i in range(1, N - 1):
    t[i] = gcd(lcg[i - 1], rcg[i + 1])
t[N - 1] = lcg[N - 2]

print(max(t))
