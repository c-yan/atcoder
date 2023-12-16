N, K = map(int, input().split())
x = list(map(int, input().split()))

p = N
for i in range(N):
    if x[i] > 0:
        p = i
        break

result = float('inf')
for i in range(K + 1):
    if p - i < 0 or p + K - i > N:
        continue
    if i == 0:
        result = min(result, x[p + K - 1])
    elif i == K:
        result = min(result, -x[p - K])
    else:
        l = x[p - i]
        r = x[p + (K - i) - 1]
        result = min(result, r - 2 * l, r * 2 - l)
print(result)
