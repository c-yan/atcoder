N, *a = map(int, open(0).read().split())

pos = [0] * (N + 1)
for i in range(N):
    pos[a[i]] = i

l = [-1] * N
r = [-1] * N
result = 0
for x in range(N, 0, -1):
    i = pos[x]

    j = i
    while j != 0 and a[j - 1] > x:
        j = l[j - 1]
    l[i] = j

    j = i
    while j != N - 1 and a[j + 1] > x:
        j = r[j + 1]
    r[i] = j

    result += x * (i - l[i] + 1) * (r[i] - i + 1)
print(result)
