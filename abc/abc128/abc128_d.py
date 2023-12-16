N, K = map(int, input().split())
V = list(map(int, input().split()))

m = min(N, K)
result = 0
for i in range(m + 1):
    for j in range(i + 1):
        t = V[:j]
        t.extend(V[N - (i - j):])
        t.sort(reverse=True)
        l = K - i
        while len(t) > 0 and l > 0 and t[-1] < 0:
            t.pop()
            l -= 1
        result = max(result, sum(t))
print(result)
