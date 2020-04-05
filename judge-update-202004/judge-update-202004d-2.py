from math import gcd

N, Q = map(int, input().split())
A = list(map(int, input().split()))
S = list(map(int, input().split()))

for i in range(N - 1):
    A[i + 1] = gcd(A[i + 1], A[i])

for i in range(Q):
    X = S[i]
    t = gcd(A[-1], X)
    if t != 1:
        print(t)
    else:
        ng = -1
        ok = N - 1
        while ok - ng > 1:
            m = (ok + ng) // 2
            if gcd(X, A[m]) == 1:
                ok = m
            else:
                ng = m
        print(ok + 1)
