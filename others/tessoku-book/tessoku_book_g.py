from sys import stdin
from itertools import accumulate

readline = stdin.readline

D = int(readline())
N = int(readline())
result = [0] * (D + 1)
for _ in range(N):
    L, R = map(int, readline().split())
    result[L - 1] += 1
    result[R] -= 1
print(*list(accumulate(result))[:-1], sep='\n')
