from sys import stdin
from collections import Counter

readline = stdin.readline

N, M = map(int, readline().split())
S = [readline()[:-1] for _ in range(N)]

c = Counter(s.count('1') % 2 for s in S)
print(c[0] * c[1])
