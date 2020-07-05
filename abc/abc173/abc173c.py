# ビット全探索
from itertools import product

H, W, K = map(int, input().split())
c = [input() for _ in range(H)]

result = 0
for a in product([True, False], repeat=H):
    for b in product([True, False], repeat=W):
        t = 0
        for y in range(H):
            if a[y]:
                continue
            for x in range(W):
                if b[x]:
                    continue
                if c[y][x] == '#':
                    t += 1
        if t == K:
            result += 1
print(result)
