N, M = map(int, input().split())
A = [input() for _ in range(2 * N)]

a = [(0, i) for i in range(2 * N)]
for i in range(M):
    t = []
    for j in range(N):
        c, d = a[j * 2]
        e, f = a[j * 2 + 1]
        c, e = -c, -e
        x = A[d][i]
        y = A[f][i]
        if x == y:
            t.append((-c, d))
            t.append((-e, f))
        elif (x == 'G' and y == 'C') or (x == 'C' and y == 'P') or (x == 'P' and y == 'G'):
            t.append((-(c + 1), d))
            t.append((-e, f))
        else:
            t.append((-c, d))
            t.append((-(e + 1), f))
    a = sorted(t)
print(*(i + 1 for _, i in a), sep='\n')
