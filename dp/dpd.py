# DP
def main():
    N, W = map(int, input().split())

    dp = [-1] * (W + 1)
    dp[0] = 0
    for _ in range(N):
        w, v = map(int, input().split())
        for i in range(W - w, -1, -1):
            dpi = dp[i]
            if dpi != -1:
                if dp[i + w] < dpi + v:
                    dp[i + w] = dpi + v
    print(max(dp))


main()
