N = int(input())
S = [input() for _ in range(N)]


def dfs(n):
    if n == 0:
        return 1

    if S[n - 1] == 'AND':
        return dfs(n - 1)
    elif S[n - 1] == 'OR':
        return 2 ** n + dfs(n - 1)


print(dfs(N))
