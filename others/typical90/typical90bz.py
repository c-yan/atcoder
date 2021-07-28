from sys import stdin

readline = stdin.readline

N, M = map(int, readline().split())
t = [0] * N
for _ in range(M):
    a, b = map(int, readline().split())
    if a > b:
        a, b = b, a
    t[b - 1] += 1
print(t.count(1))
