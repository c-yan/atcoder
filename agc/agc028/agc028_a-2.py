from fractions import gcd


def lcm(x, y):
    return x // gcd(x, y) * y


N, M = map(int, input().split())
S = input()
T = input()

for i in range(N):
    if M * i % N == 0 and S[i] != T[M * i // N]:
        print(-1)
        exit()
print(lcm(N, M))
