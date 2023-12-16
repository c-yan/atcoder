from itertools import accumulate

N, *a = map(int, open(0).read().split())

b = [0] * N
for i in range(N):
    if a[i] != i + 1:
        continue
    b[i] = 1
b = list(accumulate(b))

result = 0
for i in range(N):
    if a[i] != i + 1:
        continue
    result += b[-1] - b[i]

d = {}
for i in range(N):
    d[i + 1] = a[i]
t = 0
for i in range(1, N + 1):
    if d[i] == i:
        continue
    if d[d[i]] != i:
        continue
    t += 1
result += t // 2

print(result)
