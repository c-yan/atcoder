# 深さ優先探索
from sys import setrecursionlimit


def genid(a, b):
    if b < a:
        a, b = b, a
    return a * 100000 + b


N = int(input())
ab = [list(map(int, input().split())) for _ in range(N - 1)]

edges = [[] for _ in range(N)]
for a, b in ab:
    edges[a - 1].append(b - 1)
    edges[b - 1].append(a - 1)

colors = {}
q = [(0, -1, -1)]
while q:
    currentNode, usedColor, parentNode = q.pop()
    color = 1
    for childNode in edges[currentNode]:
        if childNode == parentNode:
            continue
        if color == usedColor:
            color += 1
        colors[genid(currentNode, childNode)] = color
        q.append((childNode, color, currentNode))
        color += 1

print(max(len(e) for e in edges))
for a, b in ab:
    print(colors[genid(a - 1, b - 1)])
