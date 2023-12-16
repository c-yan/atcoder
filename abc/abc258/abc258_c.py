from sys import stdin

readline = stdin.readline

N, Q = map(int, readline().split())
S = readline()[:-1]

i = 0
result = []
for _ in range(Q):
    t, x = map(int, readline().split())
    if t == 1:
        i -= x
    elif t == 2:
        result.append(S[(i + x - 1) % len(S)])
print(*result, sep='\n')
