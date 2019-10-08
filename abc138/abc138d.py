N, Q = map(int, input().split())

values = [0] * N
links = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    links[a - 1].append(b - 1)
    links[b - 1].append(a - 1)
for _ in range(Q):
    p, x = map(int, input().split())
    values[p - 1] += x

s = [(0, -1)]
while s:
    i, p = s.pop()
    for j in links[i]:
        if j == p:
            continue
        values[j] += values[i]
        s.append((j, i))
print(*values)
