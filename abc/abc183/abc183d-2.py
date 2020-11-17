N, W = map(int, input().split())

t = {}
for _ in range(N):
    S, T, P = map(int, input().split())
    t.setdefault(S, 0)
    t[S] += P
    t.setdefault(T, 0)
    t[T] -= P

c = 0
for k in sorted(t):
    c += t[k]
    if c <= W:
        continue
    print('No')
    break
else:
    print('Yes')
