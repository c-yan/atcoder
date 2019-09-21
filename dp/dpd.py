from sys import stdin


def main():
    from builtins import int, range
    readline = stdin.readline
    n, w = map(int, readline().split())
    t = [-1] * (w + 1)
    t[w] = 0
    for _ in range(n):
        nw, nv = map(int, readline().split())
        for i in range(nw, w + 1):
            ti = t[i]
            if ti == -1:
                continue
            if t[i - nw] < ti + nv:
                t[i - nw] = ti + nv
    print(max(t))


main()
