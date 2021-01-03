# imos 法
from sys import stdin
from itertools import accumulate

readline = stdin.readline

n = int(readline())

t = [0] * (1000000 + 2)
for _ in range(n):
    a, b = map(int, readline().split())
    t[a] += 1
    t[b + 1] -= 1
print(max(accumulate(t[:-1])))
