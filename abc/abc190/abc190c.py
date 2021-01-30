from itertools import product

N, M = map(int, input().split())
AB = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(M)]
K = int(input())
CD = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(K)]

result = 0
for p in product(range(2), repeat=K):
    t = [False] * N
    for i in range(K):
        t[CD[i][p[i]]] = True
    c = 0
    for a, b in AB:
        if t[a] and t[b]:
            c += 1
    result = max(result, c)
print(result)
