N = int(input())
a = [int(input()) for _ in range(N)]

d = {}
for i, j in enumerate(sorted(set(a))):
    d[j] = i

for e in a:
    print(d[e])
