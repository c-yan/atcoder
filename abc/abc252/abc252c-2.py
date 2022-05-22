N = int(input())
S = [[int(c) for c in input()] for _ in range(N)]

result = 10 ** 15
for i in range(10):
    t = {}
    for j in range(N):
        x = S[j].index(i)
        t.setdefault(x, 0)
        t[x] += 1
    result = min(result, max(k + (t[k] - 1) * 10 for k in t))
print(result)
