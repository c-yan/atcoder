S, P = map(int, input().split())

for N in range(1, int(P ** 0.5) + 1):
    if P % N != 0:
        continue
    M = P // N
    if N + M == S:
        print('Yes')
        break
else:
    print('No')
