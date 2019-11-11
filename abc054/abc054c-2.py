# 解説の C++ のコードを Python に移植
nmax = 8
graph = [[False] * nmax for _ in range(nmax)]


def dfs(v, N, visited):
    all_visited = True
    for i in range(N):
        if not visited[i]:
            all_visited = False
    if all_visited:
        return 1

    ret = 0
    for i in range(N):
        if not graph[v][i]:
            continue
        if visited[i]:
            continue

        visited[i] = True
        ret += dfs(i, N, visited)
        visited[i] = False
    return ret


N, M = map(int, input().split())
for _ in range(M):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = graph[b - 1][a - 1] = True

visited = [False] * nmax
visited[0] = True
print(dfs(0, N, visited))
