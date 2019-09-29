def read_key():
    a, _ = map(int, input().split())
    m = 0
    for c in map(int, input().split()):
        m |= 1 << (c - 1)
    return (a, m)


def main():
    INF = float('inf')

    N, M = map(int, input().split())
    keys = [read_key() for _ in range(M)]

    dp = [[INF] * (1 << N) for _ in range(M + 1)]

    dp[0][0] = 0
    for i in range(M):
        a, m = keys[i]
        dpi = dp[i]
        dpi1 = dpi[i + 1]
        for j in range(1 << N):
            if dpi[j] == INF:
                continue
            if dpi[j] + a < dpi1[j | m]:
                dpi1[j | m] = dpi[j] + a
            if dpi[j] < dpi1[j]:
                dpi1[j] = dpi[j]

    if dp[M][(1 << N) - 1] == INF:
        print(-1)
    else:
        print(dp[M][(1 << N) - 1])


main()
