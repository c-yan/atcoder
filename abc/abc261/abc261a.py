L1, R1, L2, R2 = map(int, input().split())

a = [0] * 100
for x in range(L1, R1):
    a[x] += 1
for x in range(L2, R2):
    a[x] += 1
print(a.count(2))
