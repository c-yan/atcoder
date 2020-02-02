# 深さ優先探索
N, u, v = map(int, input().split())

if u == v:
    print(0)
    exit()

edges = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    A, B = map(int, input().split())
    edges[A].append(B)
    edges[B].append(A)


def calc_destination(start, edges):
    destination = [-1] * (N + 1)
    destination[start] = 0
    q = [start]
    while len(q) != 0:
        current = q.pop()
        for n in edges[current]:
            if destination[n] != -1:
                continue
            destination[n] = destination[current] + 1
            q.append(n)
    return destination


tak = calc_destination(u, edges)
aok = calc_destination(v, edges)

result = 0
for i in range(1, N + 1):
    aoki = aok[i]
    if tak[i] >= aoki:
        continue
    if aoki > result:
        result = aoki
print(result - 1)
