# Union Find 木
from sys import stdin


def main():
    def find(parent, i):
        t = parent[i]
        if t == -1:
            return i
        t = find(parent, t)
        parent[i] = t
        return t

    def unite(parent, i, j):
        i = find(parent, i)
        j = find(parent, j)
        if i == j:
            return
        parent[i] = j

    from builtins import int, map, range
    readline = stdin.readline

    n, q = map(int, readline().split())
    parent = [-1] * n

    for _ in range(q):
        p, a, b = map(int, readline().split())
        if p == 0:
            unite(parent, a, b)
        else:
            if find(parent, a) == find(parent, b):
                print('Yes')
            else:
                print('No')


main()
