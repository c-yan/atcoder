N, M, *a = map(int, open(0).read().split())

t = list(range(N - 1, -1, -1))
for i in range(M):
    t[a[i] - 1] = N + i

print(*[e[1] for e in sorted([(t[i], i + 1) for i in range(N)], reverse=True)], sep='\n')
