N, M = map(int, input().split())


def conv(S):
    result = 0
    for c in S:
        result *= 2
        if c == 'Y':
            result += 1
    return result


dp = [-1] * 2001
dp[0] = 0
for _ in range(M):
    S, C = input().split()
    S = conv(S)
    C = int(C)
    for i in range(2000, -1, -1):
        if dp[i] == -1:
            continue
        if dp[i | S] == -1 or dp[i | S] > dp[i] + C:
            dp[i | S] = dp[i] + C
print(dp[(1 << N) - 1])
