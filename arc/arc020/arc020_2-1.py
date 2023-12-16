from collections import Counter

n, c, *a = map(int, open(0).read().split())

c1 = Counter(a[::2])
c2 = Counter(a[1::2])

for i in range(1, 11):
    if i not in c1:
        c1[i] = 0
    if i not in c2:
        c2[i] = 0

a = c1.most_common(2)
b = c2.most_common(2)

x = (n + 1) // 2
y = n - x

if a[0][0] != b[0][0]:
    print(((x - a[0][1]) + (y - b[0][1])) * c)
else:
    m = ((x - a[0][1]) + (y - b[1][1])) * c
    n = ((x - a[1][1]) + (y - b[0][1])) * c
    print(min(m, n))
