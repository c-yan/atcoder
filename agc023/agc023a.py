N = int(input())
A = list(map(int, input().split()))

c = [0] * (N + 1)
for i in range(N):
    c[i + 1] = c[i] + A[i]

d = {}
for i in range(1, N + 1):
    if c[i] not in d:
        d[c[i]] = 1
    else:
        d[c[i]] += 1

result = 0
if 0 in d:
    result += d[0]
for k in d:
    if d[k] != 1:
        result += d[k] * (d[k] - 1) // 2
print(result)
