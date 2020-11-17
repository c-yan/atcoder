def main():
    H, W = map(int, input().split())
    A = [input() for _ in range(H)]

    t = [list(a) for a in A]
    q = []
    c = 0
    for h in range(H):
        for w in range(W):
            if A[h][w] == '#':
                q.append((h, w))
            elif A[h][w] == '.':
                c += 1

    result = 0
    while c != 0:
        nq = []
        for h, w in q:
            if h != 0 and t[h - 1][w] == '.':
                t[h - 1][w] = '#'
                c -= 1
                nq.append((h - 1, w))
            if h != H - 1 and t[h + 1][w] == '.':
                t[h + 1][w] = '#'
                c -= 1
                nq.append((h + 1, w))
            if w != 0 and t[h][w - 1] == '.':
                t[h][w - 1] = '#'
                c -= 1
                nq.append((h, w - 1))
            if w != W - 1 and t[h][w + 1] == '.':
                t[h][w + 1] = '#'
                c -= 1
                nq.append((h, w + 1))
        q = nq
        result += 1
    print(result)


main()
