from sys import setrecursionlimit


def f(i, links, dp):
    if dp[i] != -1:
        return dp[i]
    if len(links[i]) == 0:
        dp[i] = 0
    else:
        dp[i] = max(f(j, links, dp) for j in links[i]) + 1
    return dp[i]


setrecursionlimit(1000000)

N, M = map(int, input().split())

links = [[] for _ in range(N)]
for _ in range(M):
    x, y = map(int, input().split())
    links[x - 1].append(y - 1)

dp = [-1] * N
print(max(f(i, links, dp) for i in range(N)))
