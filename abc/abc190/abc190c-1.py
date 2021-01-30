from itertools import product

N, M = map(int, input().split())
AB = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(M)]
K = int(input())
CD = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(K)]

result = 0
for p in product(*CD):
    s = set(p)
    c = 0
    for a, b in AB:
        if a in s and b in s:
            c += 1
    result = max(result, c)
print(result)
