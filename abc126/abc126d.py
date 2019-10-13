N = int(input())

link = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v, w = map(int, input().split())
    link[u - 1].append((v - 1, w))
    link[v - 1].append((u - 1, w))

d = [0] * N
q = [0]
while q:
    p = q.pop()
    for n, w in link[p]:
        if d[n] == 0:
            d[n] = d[p] + w
            q.append(n)

for i in d:
    print(i % 2)
