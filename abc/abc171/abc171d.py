from sys import stdin
readline = stdin.readline

N = int(readline())
A = list(map(int, readline().split()))
Q = int(readline())

t = [0] * (10 ** 5 + 1)
s = sum(A)
for a in A:
    t[a] += 1

for _ in range(Q):
    B, C = map(int, readline().split())
    s -= B * t[B]
    s += C * t[B]
    t[C] += t[B]
    t[B] = 0
    print(s)
