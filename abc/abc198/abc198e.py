from sys import setrecursionlimit, stdin

readline = stdin.readline
setrecursionlimit(10 ** 6)

N = int(readline())
C = list(map(int, readline().split()))

links = [[] for _ in range(N)]
for _ in range(N - 1):
    A, B = map(lambda x: int(x) - 1, readline().split())
    links[A].append(B)
    links[B].append(A)

dp = [(10 ** 18, False)] * N
dp[0] = (0, True)

def f(frm, to, steps, colors):
    if steps == dp[to][0]:
        if C[to] not in colors:
            dp[to] = (steps, True)
    elif steps < dp[to][0]:
        dp[to] = (steps, C[to] not in colors)
    colors.setdefault(C[to], 0)
    colors[C[to]] += 1
    for nto in links[to]:
        if nto == frm:
            continue
        f(to, nto, steps + 1, colors)
    colors[C[to]] -= 1
    if colors[C[to]] == 0:
        del colors[C[to]]

f(-1, 0, 0, {})
result = []
for i in range(N):
    if dp[i][1]:
        result.append(i + 1)
print(*result, sep='\n')
