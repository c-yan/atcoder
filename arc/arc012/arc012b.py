N, va, vb, L = map(int, input().split())

for _ in range(N):
    L = (L / va) * vb
print(L)
