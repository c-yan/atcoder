n, c, *a = map(int, open(0).read().split())

c1 = {}
c2 = {}
for i in range(1, 11):
    c1[i] = 0
    c2[i] = 0
for x in a[::2]:
    c1[x] += 1
for x in a[1::2]:
    c2[x] += 1

result = float('inf')
x = (n + 1) // 2
y = n - x
for i in range(1, 10):
    for j in range(i + 1, 11):
        result = min(result, ((x - c1[i]) + (y - c2[j])) * c)
        result = min(result, ((x - c1[j]) + (y - c2[i])) * c)
print(result)
