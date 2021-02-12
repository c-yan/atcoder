from sys import stdin
from math import gcd

readline = stdin.readline

N = int(readline())

A, B = map(int, readline().split())
t = [A, B]
for _ in range(N - 1):
    A, B = map(int, readline().split())
    u = []
    for x in t:
        u.append(gcd(x, A))
        u.append(gcd(x, B))
    u.sort()
    t = []
    for i in range(len(u)):
        for j in range(i + 1, len(u)):
            if u[j] % u[i] == 0:
                break
        else:
            t.append(u[i])
print(max(t))
