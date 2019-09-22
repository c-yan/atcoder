from sys import exit, setrecursionlimit


def get_node_id(i, j, node_id_db):
    if i < j:
        return node_id_db[i][j]
    else:
        return node_id_db[j][i]


def dfs(node_id, edges, dp):
    t = dp[node_id]
    if t >= 0:
        return t
    dp[node_id] = 0
    result = 0
    for n in edges[node_id]:
        t = dfs(n, edges, dp)
        if t == 0:  # looped
            print(-1)
            exit()
        if t > result:
            result = t
    result += 1
    dp[node_id] = result
    return result


def main():
    N = int(input())
    A = [[int(e) - 1 for e in input().split()] for _ in range(N)]

    node_id_db = [[0] * N for _ in range(N)]
    v = 0
    for i in range(N):
        for j in range(i + 1, N):
            node_id_db[i][j] = v
            v += 1

    start_nodes = []
    edges = [[] for _ in range(N * (N - 1) // 2)]
    for i in range(N):
        Ai = A[i]
        from_id = get_node_id(i, Ai[0], node_id_db)
        if i < Ai[0]:
            start_nodes.append(from_id)
        for j in range(1, N - 1):
            to_id = get_node_id(i, Ai[j], node_id_db)
            edges[from_id].append(to_id)
            from_id = to_id

    dp = [-1 for _ in range(N * (N - 1) // 2)]
    print(max(dfs(n, edges, dp) for n in start_nodes))


setrecursionlimit(1000000)
main()
