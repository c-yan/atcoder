from sys import stdin

readline = stdin.readline

H, W, N = map(int, readline().split())

a = set()
b = set()
c = []
for i in range(N):
    A, B = map(int, readline().split())
    a.add(A)
    b.add(B)
    c.append((A, B))

aa = {}
for i, v in enumerate(sorted(a)):
    aa[v] = i + 1
bb = {}
for i, v in enumerate(sorted(b)):
    bb[v] = i + 1

result = []
for x, y in c:
    result.append('%d %d' % (aa[x], bb[y]))
print(*result, sep='\n')
