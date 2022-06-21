from sys import stdin
from itertools import accumulate

readline = stdin.readline

N = int(readline())

t = [0] * (2 * 10 ** 5 + 1)
for _ in range(N):
    L, R = map(int, readline().split())
    t[L] += 1
    t[R] -= 1
a = [x != 0 for x in accumulate(t)]

result = []
j = -1
while True:
    try:
        i = a.index(True, j + 1)
    except:
        break
    j = a.index(False, i + 1)
    result.append((i, j))
print(*("%d %d" % (x, y) for x, y in result), sep='\n')
