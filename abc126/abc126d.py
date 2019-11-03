N = int(input())

link = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v, w = map(int, input().split())
    link[u - 1].append((v - 1, w))
    link[v - 1].append((u - 1, w))

d = [-1] * N
d[0] = 0
q = [0]
while q:
    p = q.pop()
    for n, w in link[p]:
        if d[n] == -1:
            d[n] = d[p] + w
            q.append(n)

for i in d:
    print(i % 2)
