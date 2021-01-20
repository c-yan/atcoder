n, x = map(int, input().split())
x -= 1
h = list(map(int, input().split()))

links = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    links[a].append(b)
    links[b].append(a)


def dfs(i, p):
    result = 0
    for j in links[i]:
        if j == p:
            continue
        result += dfs(j, i)
    if result != 0 or h[i] == 1:
        result += 2
    return result


print(sum(dfs(i, x) for i in links[x]))
