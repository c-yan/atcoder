from sys import stdin

readline = stdin.readline

N = int(readline())
XY = [tuple(map(int, readline().split())) for _ in range(N)]
S = readline()[:-1]

L = {}
R = {}
for i in range(N):
    X, Y = XY[i]
    if S[i] == 'L':
        if Y in L:
            L[Y] = max(L[Y], X)
        else:
            L[Y] = X
    elif S[i] == 'R':
        if Y in R:
            R[Y] = min(R[Y], X)
        else:
            R[Y] = X

for k in L:
    if k not in R:
        continue
    if L[k] > R[k]:
        print('Yes')
        exit()
print('No')
