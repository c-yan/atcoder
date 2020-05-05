L, R = map(int, input().split())

m = 2019
for i in range(L, R):
    for j in range(i + 1, R + 1):
        t = (i * j) % 2019
        if t < m:
            m = t
        if m == 0:
            break
    if m == 0:
        break
print(m)
