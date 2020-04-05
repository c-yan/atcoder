from math import gcd

N, Q = map(int, input().split())
A = list(map(int, input().split()))
S = list(map(int, input().split()))

gcd_a = A[0]
a = [(1, A[0])]
for i in range(1, N):
    t = gcd(gcd_a, A[i])
    if t != gcd_a:
        gcd_a = t
        a.append((i + 1, gcd_a))

for i in range(Q):
    X = S[i]
    t = gcd(gcd_a, X)
    if t != 1:
        print(t)
    else:
        for j, g in a:
            if gcd(X, g) != 1:
                continue
            print(j)
            break
