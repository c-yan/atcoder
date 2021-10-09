from sys import stdin

readline = stdin.readline

N = int(readline())

a = []
for _ in range(N):
    A, B = map(int, readline().split())
    a.append((A, 1))
    a.append((A + B, -1))
a.sort()

c = 0
p = 0
D = [0] * (N + 1)
for x, y in a:
    D[c] += x - p
    c += y
    p = x
print(*D[1:])
