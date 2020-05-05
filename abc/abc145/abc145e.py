def main():
    N, T = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]

    dp = [-1] * (T + 3000)
    dp[0] = 0
    for a, b in sorted(AB):
        for i in range(T - 1, -1, -1):
            if dp[i] == -1:
                continue
            if dp[i + a] < dp[i] + b:
                dp[i + a] = dp[i] + b
    print(max(dp))


main()
