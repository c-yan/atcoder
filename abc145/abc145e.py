def main():
    N, T = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]

    dp = [-1] * (T + 3000)
    dp[0] = 0
    for a, b in sorted(AB):
        for j in range(T - 1, -1, -1):
            if dp[j] == -1:
                continue
            if dp[j] + b > dp[j + a]:
                dp[j + a] = dp[j] + b
    print(max(dp))


main()
