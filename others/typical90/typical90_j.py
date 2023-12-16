from sys import stdin
from itertools import accumulate

readline = stdin.readline

N = int(readline())

a = [[0] * (N + 1) for _ in range(2)]
for i in range(N):
    C, P = map(int, readline().split())
    a[C - 1][i + 1] = P
a = [list(accumulate(x)) for x in a]

Q = int(readline())

result = []
for _ in range(Q):
    A, B = map(int, readline().split())
    result.append('%d %d' % (a[0][B] - a[0][A - 1], a[1][B] - a[1][A - 1]))
print(*result, sep='\n')
