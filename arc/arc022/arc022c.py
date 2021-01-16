from sys import setrecursionlimit, stdin

readline = stdin.readline
setrecursionlimit(10 ** 6)

N = int(readline())

links = [[] for _ in range(N)]
for _ in range(N - 1):
    A, B = map(int, readline().split())
    links[A - 1].append(B - 1)
    links[B - 1].append(A - 1)


def dfs(c, p, d):
    result = (d, c)
    for a in links[c]:
        if a == p:
            continue
        result = max(result, dfs(a, c, d + 1))
    return result


x = max(dfs(c, 0, 1) for c in links[0])[1]
y = max(dfs(c, x, 1) for c in links[x])[1]
print(x + 1, y + 1)
