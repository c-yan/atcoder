from sys import stdin, setrecursionlimit


def euler_tour(n, i):
    left[n] = i
    i += 1
    for c in children[n]:
        i = euler_tour(c, i)
    right[n] = i
    return i

readline = stdin.readline
setrecursionlimit(10 ** 6)

N = int(readline())

root = -1
children = [[] for _ in range(N)]
for i in range(N):
    p = int(readline())
    if p == -1:
        root = i
    else:
        children[p - 1].append(i)

left = [0] * N
right = [0] * N
euler_tour(root, 0)

Q = int(readline())
result = []
for _ in range(Q):
    a, b = map(lambda x: int(x) - 1, readline().split())
    if left[b] < left[a] < right[b]:
        result.append('Yes')
    else:
        result.append('No')
print(*result, sep='\n')
