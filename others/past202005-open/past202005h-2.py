N, L = map(int, input().split())
x = set(map(int, input().split()))
T1, T2, T3 = map(int, input().split())

dp = [float('inf')] * (L + 4)
dp[0] = 0
for i in range(L):
    a = dp[i] + T1
    if i + 1 in x:
        a += T3
    if dp[i + 1] > a:
        dp[i + 1] = a

    a = dp[i] + T1 + T2
    if i + 2 in x:
        a += T3
    if dp[i + 2] > a:
        dp[i + 2] = a

    a = dp[i] + T1 + T2 * 3
    if i + 4 in x:
        a += T3
    if dp[i + 4] > a:
        dp[i + 4] = a

result = dp[L]
result = min(result, dp[L - 1] + T1 // 2 + T2 // 2)
result = min(result, dp[L - 2] + T1 // 2 + 3 * T2 // 2)
result = min(result, dp[L - 3] + T1 // 2 + 5 * T2 // 2)
print(result)
