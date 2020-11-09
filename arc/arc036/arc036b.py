N, *h = map(int, open(0).read().split())

result = 1
s = 0
while s != N - 1:
    t = s
    while t < N - 1 and h[t] < h[t + 1]:
        t += 1
    u = t
    while u < N - 1 and h[u] > h[u + 1]:
        u += 1
    result = max(result, u - s + 1)
    s = u
print(result)
