from sys import setrecursionlimit, stdin

readline = stdin.readline
setrecursionlimit(10 ** 6)

N = int(readline())

links = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    A, B = map(int, readline().split())
    links[A].append(B)
    links[B].append(A)

for l in links:
    l.sort(reverse=True)

def dfs(n):
    result.append(n)
    visited.add(n)
    while links[n]:
        i = links[n].pop()
        if i in visited:
            continue
        dfs(i)
        result.append(n)


visited = set()
result = []
dfs(1)
print(*result)
