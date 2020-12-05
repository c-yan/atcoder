N, *a = map(int, open(0).read().split())

d = {}
for i in range(N):
    d[a[i]] = i + 1

c = 0
for i in range(N):
    if a[i] == i + 1:
        continue
    j = d[i + 1] - 1
    x, y = a[i], a[j]
    a[i], a[j] = y, x
    d[a[i]] = i + 1
    d[a[j]] = j + 1
    c += 1

if N < c or (N - c) % 2 == 1:
    print('NO')
else:
    print('YES')
