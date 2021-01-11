from sys import stdin

readline = stdin .readline

N, C = map(int, readline().split())

q = []
for _ in range(N):
    a, b, c = map(int, readline().split())
    q.append((a, c))
    q.append((b + 1, -c))

result = 0
p = 0
ac = 0
for x, y in sorted(q):
    result += min(C, ac) * (x - p)
    p = x
    ac += y
print(result)
