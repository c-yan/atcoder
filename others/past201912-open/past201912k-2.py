from sys import setrecursionlimit


def euler_tour(n, i, left, right):
    left[n] = i
    i += 1
    for c in children[n]:
        i = euler_tour(c, i, left, right)
    right[n] = i
    return i


setrecursionlimit(10 ** 6)

N = int(input())

root = -1
children = [[] for _ in range(N + 1)]
left = [0] * (N + 1)
right = [0] * (N + 1)

for i in range(1, N + 1):
    p = int(input())
    if p == -1:
        root = i
    else:
        children[p].append(i)

euler_tour(root, 0, left, right)

Q = int(input())
result = []
for _ in range(Q):
    a, b = map(int, input().split())
    if left[b] < left[a] < right[b]:
        result.append('Yes')
    else:
        result.append('No')
print(*result, sep='\n')
