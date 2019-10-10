# DP
def main():
    N, W = map(int, input().split())

    dp = [-1] * (W + 1)
    dp[0] = 0
    for _ in range(N):
        w, v = map(int, input().split())
        for i in range(W - w, -1, -1):
            if dp[i] == -1:
                continue
            if dp[i + w] < dp[i] + v:
                dp[i + w] = dp[i] + v
    print(max(dp))


main()
