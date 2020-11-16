N, M = map(int, input().split())

t = [1 << i for i in range(N)]
for _ in range(M):
    x, y = map(lambda x: int(x) - 1, input().split())
    a = (1 << x) | (1 << y)
    t[x] |= a
    t[y] |= a

result = 0
for i in range(1 << N):
    for j in range(N):
        if (i >> j) & 1 == 0:
            continue
        if t[j] & i != i:
            break
    else:
        result = max(result, bin(i).count('1'))
print(result)
