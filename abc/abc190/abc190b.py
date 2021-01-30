N, S, D = map(int, input().split())

for _ in range(N):
    X, Y = map(int, input().split())
    if X >= S:
        continue
    if Y <= D:
        continue
    print('Yes')
    break
else:
    print('No')
