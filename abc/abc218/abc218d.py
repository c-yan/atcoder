N = int(input())
xy = [tuple(map(int, input().split())) for _ in range(N)]

a = set()
b = set()
for x, y in xy:
    a.add(x)
    b.add(y)
c = sorted(a)
d = sorted(b)
e = {}
f = {}
for i in range(len(c)):
    e[c[i]] = i
for i in range(len(d)):
    f[d[i]] = i

xy = [(e[x], f[y]) for x, y in xy]

t = [set() for _ in range(len(c))]
for x, y in xy:
    t[x].add(y)

result = 0
for i in range(len(c)):
    for j in range(i + 1, len(c)):
        g = len(t[i] & t[j])
        result += g * (g - 1) // 2
print(result)
