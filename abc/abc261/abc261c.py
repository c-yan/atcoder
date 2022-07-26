from sys import stdin

readline = stdin.readline

N = int(readline())

result = []
d = {}
for _ in range(N):
    S = readline()[:-1]
    if S not in d:
        result.append(S)
        d[S] = 1
    else:
        result.append('%s(%d)' % (S, d[S]))
        d[S] += 1
print(*result, sep='\n')
