from sys import stdin

readline = stdin.readline

N, A, B = map(int, readline().split())
S = [int(readline()) for _ in range(N)]

mi = min(S)
ma = max(S)

if ma == mi:
    print(-1)
    exit()

P = B / (ma - mi)
Q = A - P * (sum(S) / N)

print(P, Q)
