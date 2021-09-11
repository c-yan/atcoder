N = int(input())
xy = [tuple(map(int, input().split())) for _ in range(N)]

d = {}
for x, y in xy:
    d.setdefault(x, set())
    d[x].add(y)
t = list(d.values())

result = 0
for i in range(len(t)):
    for j in range(i + 1, len(t)):
        n = len(t[i] & t[j])
        result += n * (n - 1) // 2
print(result)
