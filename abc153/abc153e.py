def main():
    from sys import stdin
    readline = stdin.readline
    H, N = map(int, readline().split())
    AB = [list(map(int, readline().split())) for _ in range(N)]

    max_A = max(a for a, _ in AB)
    inf = float('inf')
    dp = [inf] * (H + max_A + 1)
    dp[0] = 0
    for i in range(H):
        if dp[i] == inf:
            continue
        for a, b in AB:
            t = dp[i] + b
            if t < dp[i + a]:
                dp[i + a] = t
    print(min(dp[H:]))


main()
