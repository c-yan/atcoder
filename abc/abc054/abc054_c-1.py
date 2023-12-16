def f(i, links, visited, nodes):
    t = 1 << i
    if t & visited != 0:
        return 0
    visited |= t
    if visited == (1 << nodes) - 1:
        return 1
    result = 0
    for j in links[i]:
        result += f(j, links, visited, nodes)
    return result


N, M = map(int, input().split())

links = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    links[a - 1].append(b - 1)
    links[b - 1].append(a - 1)

result = 0
for i in links[0]:
    result += f(i, links, 1, N)
print(result)
