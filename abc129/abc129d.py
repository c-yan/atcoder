def main():
    from sys import stdin
    from builtins import range

    readline = stdin.readline

    H, W = map(int, readline().split())
    S = [readline()[:-1] + '#' for _ in range(H)]

    S.append('#' * W)
    ft = [[i] * i for i in range(100)]
    yoko = [[0] * W for _ in range(H)]
    for i in range(H):
        start = -1
        si = S[i]
        yokoi = yoko[i]
        for j in range(W + 1):
            if si[j] == '#':
                if start != -1:
                    t = j - start
                    if t < 100:
                        yokoi[start:j] = ft[t]
                    else:
                        yokoi[start:j] = [t] * t
                    start = -1
            else:
                if start == -1:
                    start = j

    result = 0
    for i in range(W):
        start = -1
        for j in range(H + 1):
            if S[j][i] == '#':
                if start != -1:
                    t = yoko_max + j - start - 1
                    if t > result:
                        result = t
                    start = -1
            else:
                yji = yoko[j][i]
                if start == -1:
                    start = j
                    yoko_max = yji
                else:
                    if yji > yoko_max:
                        yoko_max = yji
    print(result)


main()
