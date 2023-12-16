from itertools import product
from sys import stdin
readline = stdin.readline

N, M = map(int, readline().split())
xyz = [tuple(map(int, readline().split())) for _ in range(N)]

result = 0
for s in product([1, -1], repeat=3):
    xyz.sort(reverse=True, key=lambda e: s[0] * e[0] + s[1] * e[1] + s[2] * e[2])
    cx, cy, cz = 0, 0, 0
    for x, y, z in xyz[:M]:
        cx += x
        cy += y
        cz += z
    result = max(result, abs(cx) + abs(cy) + abs(cz))
print(result)
