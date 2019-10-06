N, M = map(int, input().split())

from1 = set()
toN = set()
for _ in range(M):
    a, b = map(int, input().split())
    if a == 1:
        from1.add(b)
    elif b == N:
        toN.add(a)
if from1 & toN:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')
