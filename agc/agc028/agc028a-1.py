from fractions import gcd


def lcm(x, y):
    return x // gcd(x, y) * y


N, M = map(int, input().split())
S = input()
T = input()

L = lcm(N, M)
X = {}

for i in range(N):
    X[(L // N) * i] = S[i]

for i in range(M):
    if (L // M) * i in X and X[(L // M) * i] != T[i]:
        print(-1)
        exit()
print(L)
