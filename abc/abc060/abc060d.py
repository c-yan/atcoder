from sys import stdin
from itertools import accumulate
readline = stdin.readline

N, W = map(int, input().split())
vs = [[] for _ in range(4)]
w, v = map(int, input().split())
w1 = w
vs[0].append(v)
for _ in range(N - 1):
    w, v = map(int, input().split())
    vs[w - w1].append(v)

for i in range(4):
    vs[i].sort(reverse=True)
    vs[i] = list(accumulate(vs[i]))

result = 0
for i in range(len(vs[0]) + 1):
    a = W - w1 * i
    if a < 0:
        break
    for j in range(len(vs[1]) + 1):
        b = a - (w1 + 1) * j
        if b < 0:
            break
        for k in range(len(vs[2]) + 1):
            c = b - (w1 + 2) * k
            if c < 0:
                break
            t = 0
            if i != 0:
              t += vs[0][i - 1]
            if j != 0:
              t += vs[1][j - 1]
            if k != 0:
              t += vs[2][k - 1]
            for l in range(len(vs[3]) + 1):
                d = c - (w1 + 3) * l
                if d < 0:
                    break
                if l == 0:
                    result = max(result, t)
                else:
                    result = max(result, t + vs[3][l -1])
print(result)
