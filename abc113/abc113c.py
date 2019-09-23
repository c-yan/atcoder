# 二分探索
def main():
    from sys import stdin
    from bisect import bisect_left
    readline = stdin.readline
    n, m = map(int, readline().split())
    data = [list(map(int, readline().split())) for _ in range(m)]
    t = [[] for _ in range(n)]
    for p, y in data:
        t[p - 1].append(y)
    for i in range(n):
        t[i].sort()
    for p, y in data:
        nth = bisect_left(t[p - 1], y) + 1
        print('%06d%06d' % (p, nth))


main()
