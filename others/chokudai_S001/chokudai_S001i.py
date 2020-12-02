N, *a = map(int, open(0).read().split())

i, j = 0, 0
c = 0
result = 0
while j < N:
    if c <= N:
        c += a[j]
        j += 1
    else:
        c -= a[i]
        i += 1
    if c == N:
        result += 1
while i < N:
    c -= a[i]
    i += 1
    if c == N:
        result += 1

print(result)
