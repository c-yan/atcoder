# 深さ優先探索
N = int(input())
links = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b, c = map(int, input().split())
    links[a].append((b, c))
    links[b].append((a, c))

Q, K = map(int, input().split())

d = [float('inf')] * (N + 1)
d[K] = 0
q = [K]
while q:
    i = q.pop()
    for j, c in links[i]:
        if d[i] + c < d[j]:
            d[j] = d[i] + c
            q.append(j)

result = []
for _ in range(Q):
    x, y = map(int, input().split())
    result.append(d[x] + d[y])
print(*result, sep='\n')
